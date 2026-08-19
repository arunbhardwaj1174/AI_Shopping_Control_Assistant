import customtkinter as ctk


class ResultFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="Prediction Result",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.title_label.grid(row=0, column=0, sticky="w", padx=12, pady=(12, 8))

        self.status_label = ctk.CTkLabel(
            self,
            text="Enter values and click Predict Regret.",
            font=ctk.CTkFont(size=16),
            wraplength=420,
            justify="left",
        )
        self.status_label.grid(row=1, column=0, sticky="w", padx=12, pady=(0, 10))

        self.details_label = ctk.CTkLabel(
            self,
            text="",
            anchor="w",
            justify="left",
            wraplength=420,
        )
        self.details_label.grid(row=2, column=0, sticky="w", padx=12, pady=(0, 10))

        self.advice_label = ctk.CTkLabel(
            self,
            text="",
            anchor="w",
            justify="left",
            wraplength=420,
            text_color="#1a73e8",
        )
        self.advice_label.grid(row=3, column=0, sticky="nsew", padx=12, pady=(0, 12))

    def update_result(self, result):
        status_text = (
            "Regret predicted. Please consider postponing this purchase."
            if result["prediction"]
            else "Low regret risk. This purchase is likely safe."
        )
        label_color = "#f44336" if result["prediction"] else "#4caf50"
        self.status_label.configure(text=status_text, text_color=label_color)

        self.details_label.configure(
            text=(
                f"Model: {result['model_name']}\n"
                f"Probability of regret: {result['probability']:.1%}\n"
                f"Confidence range: {result['confidence']:.1%}"
            )
        )
        self.advice_label.configure(text=f"Advice: {result['advice']}")
