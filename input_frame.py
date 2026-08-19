import customtkinter as ctk

from .utils.validation import parse_float, parse_int


class InputFrame(ctk.CTkFrame):
    def __init__(self, parent, command):
        super().__init__(parent)

        self.command = command
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="Purchase Input",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.title_label.grid(row=0, column=0, sticky="w", padx=12, pady=(12, 8))

        self.cost_entry = self._build_entry("Estimated cost")
        self.savings_entry = self._build_entry("Available savings")
        self.previous_purchase_entry = self._build_entry("Previous purchase count")
        self.days_since_last_purchase_entry = self._build_entry("Days since last purchase")

        self.error_label = ctk.CTkLabel(self, text="", text_color="#f44336")
        self.error_label.grid(row=8, column=0, sticky="w", padx=12, pady=(0, 8))

        self.predict_button = ctk.CTkButton(
            self,
            text="Predict Regret",
            fg_color="#1f6aa5",
            command=self.on_predict,
        )
        self.predict_button.grid(row=9, column=0, sticky="ew", padx=12, pady=(0, 12))

    def _build_entry(self, label_text):
        label = ctk.CTkLabel(self, text=label_text)
        label.grid(sticky="w", padx=12, pady=(6, 0))
        entry = ctk.CTkEntry(self)
        entry.grid(sticky="ew", padx=12, pady=(4, 0))
        return entry

    def on_predict(self):
        try:
            cost = parse_float(self.cost_entry.get(), "Estimated cost")
            savings = parse_float(self.savings_entry.get(), "Available savings")
            previous_purchase = parse_int(
                self.previous_purchase_entry.get(), "Previous purchase count"
            )
            days_since_last_purchase = parse_int(
                self.days_since_last_purchase_entry.get(), "Days since last purchase"
            )
        except ValueError as exc:
            self.error_label.configure(text=str(exc))
            return

        self.error_label.configure(text="")
        self.command(
            {
                "cost": cost,
                "savings": savings,
                "previous_purchase": previous_purchase,
                "days_since_last_purchase": days_since_last_purchase,
            }
        )
