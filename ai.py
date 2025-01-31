from typing import List
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class DeepSeekService:
    def __init__(self, model_name: str):
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map=device,
            trust_remote_code=True,
        )

        self.conversation_history: List[dict[str, str]] = []

    def excute(self, message: str) -> str:
        self.conversation_history.append({"role": "user", "content": message})
        inputs = self.tokenizer.apply_chat_template(
            self.conversation_history, add_generation_prompt=True, return_tensors="pt"
        ).to(self.model.device)

        outputs = self.model.generate(
            inputs,
            max_new_tokens=512,
            do_sample=False,
            top_k=50,
            top_p=0.95,
            num_return_sequences=1,
            eos_token_id=self.tokenizer.eos_token_id,
        )

        response = self.tokenizer.decode(
            outputs[0][len(inputs[0]) :], skip_special_tokens=True
        )

        self.conversation_history.append({"role": "assistant", "content": response})
        return response
