from sycophancy.utils import lookup_answer

class SycophancyAnalyser:
    def __init__(self, all_results_final_df):
        all_results_final_df["binary_neutral_validation"] = all_results_final_df["answer_neutral_validation"].apply(lambda x: lookup_answer(x, "Binary Validation Sycophancy"))
        all_results_final_df["likert_neutral_validation"] = all_results_final_df["answer_neutral_validation"].apply(lambda x: lookup_answer(x, "Likert Validation Sycophancy"))
        all_results_final_df["binary_neutral_framing"] = all_results_final_df["answer_neutral_framing"].apply(lambda x: lookup_answer(x, "Binary Framing Sycophancy"))
        all_results_final_df["likert_neutral_framing"] = all_results_final_df["answer_neutral_framing"].apply(lambda x: lookup_answer(x, "Likert Framing Sycophancy"))

        all_results_final_df["binary_positive_validation"] = all_results_final_df["answer_positive_validation"].apply(lambda x: lookup_answer(x, "Binary Validation Sycophancy"))
        all_results_final_df["likert_positive_validation"] = all_results_final_df["answer_positive_validation"].apply(lambda x: lookup_answer(x, "Likert Validation Sycophancy"))
        all_results_final_df["binary_positive_framing"] = all_results_final_df["answer_positive_framing"].apply(lambda x: lookup_answer(x, "Binary Framing Sycophancy"))
        all_results_final_df["likert_positive_framing"] = all_results_final_df["answer_positive_framing"].apply(lambda x: lookup_answer(x, "Likert Framing Sycophancy"))        

        all_results_final_df["binary_negative_validation"] = all_results_final_df["answer_negative_validation"].apply(lambda x: lookup_answer(x, "Binary Validation Sycophancy"))
        all_results_final_df["likert_negative_validation"] = all_results_final_df["answer_negative_validation"].apply(lambda x: lookup_answer(x, "Likert Validation Sycophancy"))
        all_results_final_df["binary_negative_framing"] = all_results_final_df["answer_negative_framing"].apply(lambda x: lookup_answer(x, "Binary Framing Sycophancy"))
        all_results_final_df["likert_negative_framing"] = all_results_final_df["answer_negative_framing"].apply(lambda x: lookup_answer(x, "Likert Framing Sycophancy"))

        self.all_results_final_df = all_results_final_df.drop(columns=["answer_neutral_validation", "answer_neutral_framing", "answer_positive_validation", "answer_positive_framing", "answer_negative_validation", "answer_negative_framing"])

    def validation_sycophancy(self):
        transformed = {
            "binary_neutral_validation" : self.all_results_final_df["binary_neutral_validation"].mean(),
            "binary_positive_validation" : self.all_results_final_df["binary_positive_validation"].mean(),
            "binary_negative_validation" : self.all_results_final_df["binary_negative_validation"].mean(),
            "likert_neutral_validation" : self.all_results_final_df["likert_neutral_validation"].mean(),
            "likert_positive_validation" : self.all_results_final_df["likert_positive_validation"].mean(),
            "likert_negative_validation" : self.all_results_final_df["likert_negative_validation"].mean(),
        }

        print(f"Binary validation with neutral self-description: {transformed["binary_neutral_validation"]:.2f}")
        print(f"Binary validation with positive self-description: {transformed["binary_positive_validation"]:.2f}")
        print(f"Binary validation with negative self-description: {transformed["binary_negative_validation"]:.2f}")

        print(f"Likert validation with neutral self-description: {transformed["likert_neutral_validation"]:.2f}")
        print(f"Likert validation with positive self-description: {transformed["likert_positive_validation"]:.2f}")
        print(f"Likert validation with negative self-description: {transformed["likert_negative_validation"]:.2f}")

        return transformed


    def framing_sycophancy(self):
        transformed = {
            "binary_neutral_framing" : self.all_results_final_df["binary_neutral_framing"].mean(),
            "binary_positive_framing" : self.all_results_final_df["binary_positive_framing"].mean(),
            "binary_negative_framing" : self.all_results_final_df["binary_negative_framing"].mean(),
            "likert_neutral_framing" : self.all_results_final_df["likert_neutral_framing"].mean(),
            "likert_positive_framing" : self.all_results_final_df["likert_positive_framing"].mean(),
            "likert_negative_framing" : self.all_results_final_df["likert_negative_framing"].mean(),
        }

        print(f"Binary framing with neutral self-description: {transformed["binary_neutral_framing"]:.2f}")
        print(f"Binary framing with positive self-description: {transformed["binary_positive_framing"]:.2f}")
        print(f"Binary framing with negative self-description: {transformed["binary_negative_framing"]:.2f}")

        print(f"Likert framing with neutral self-description: {transformed["likert_neutral_framing"]:.2f}")
        print(f"Likert framing with positive self-description: {transformed["likert_positive_framing"]:.2f}")
        print(f"Likert framing with negative self-description: {transformed["likert_negative_framing"]:.2f}")

        return transformed

    def validation_sycophancy_extended(self):
        print(self.all_results_final_df["binary_neutral_validation"].value_counts())
        print(self.all_results_final_df["binary_positive_validation"].value_counts())
        print(self.all_results_final_df["binary_negative_validation"].value_counts())

        print(self.all_results_final_df["likert_neutral_validation"].value_counts())
        print(self.all_results_final_df["likert_positive_validation"].value_counts())
        print(self.all_results_final_df["likert_negative_validation"].value_counts())

    def framing_sycophancy_extended(self):
        print(self.all_results_final_df["binary_neutral_framing"].value_counts())
        print(self.all_results_final_df["binary_positive_framing"].value_counts())
        print(self.all_results_final_df["binary_negative_framing"].value_counts())

        print(self.all_results_final_df["likert_neutral_framing"].value_counts())
        print(self.all_results_final_df["likert_positive_framing"].value_counts())
        print(self.all_results_final_df["likert_negative_framing"].value_counts())