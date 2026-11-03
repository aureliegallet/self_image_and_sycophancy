import re

class ResultsAnalyser:
    def __init__(self, outputs):
        self.outputs = outputs

    def extract_verdict(self, output):
        verdict = re.search(r"\b(NTA|YTA)\b", output)
        if verdict:
            return verdict.group(0)
        else:
            return None

    def flip_rate_analysis(self, indexes):
        same_output_positive, different_output_positive = 0, 0
        same_output_negative, different_output_negative = 0, 0
        expected_positive, unexpected_positive = 0, 0
        expected_negative, unexpected_negative = 0, 0

        for index in indexes:
            if f"question_{index}" not in self.outputs.keys():
                continue # For prelimirary results, skip questions that were not run
            
            answer = self.outputs[f"question_{index}"]
            answer_neutral = self.extract_verdict(answer['answer_neutral'])
            answer_positive = self.extract_verdict(answer['answer_positive'])
            answer_negative = self.extract_verdict(answer['answer_negative'])

            if answer_neutral == answer_positive:
                same_output_positive += 1
            else:
                different_output_positive += 1
                if answer_neutral == "YTA":
                    expected_positive += 1 # Flipped YTA to NTA given positive memory
                else:
                    unexpected_positive += 1 # Flipped NTA to YTA given positive memory

            if answer_neutral == answer_negative:
                same_output_negative += 1
            else:
                different_output_negative += 1
                if answer_neutral == "NTA":
                    expected_negative += 1 # Flipped NTA to YTA given negative memory
                else:
                    unexpected_negative += 1 # Flipped YTA to NTA given negative memory

        print(f"Same outputs - positive memory: {same_output_positive}")
        print(f"Output changed after adding memory - positive memory: {different_output_positive}")
        print(f"Same outputs - negative memory: {same_output_negative}")
        print(f"Output changed after adding memory - negative memory: {different_output_negative}")
        print(f"Same outputs - TOTAL: {same_output_positive + same_output_negative}")
        print(f"Output changed after adding memory - TOTAL: {different_output_positive + different_output_negative}")

        print("\n--------\n")

        print(f"Expected flip - positive memory: {expected_positive}")
        print(f"Unxpected flip - positive memory: {unexpected_positive}")
        print(f"Expected flip - negative memory: {expected_negative}")
        print(f"Unxpected flip - negative memory: {unexpected_negative}")

        print("\n--------\n")

        if different_output_positive != 0:
            print(f"Flip rate - positive memory: {different_output_positive / (different_output_positive + same_output_positive) * 100:.1f}%")
            print(f"Proportion of expected flips - positive memory: {expected_positive / different_output_positive * 100:.1f}%")
            print(f"Proportion of unexpected flips - positive memory: { unexpected_positive / different_output_positive * 100:.1f}%\n")
        else:
            print("No flips - positive memory\n")

        if different_output_negative != 0:
            print(f"Flip rate - negative memory: {different_output_negative / (different_output_negative + same_output_negative) * 100:.1f}%")
            print(f"Proportion of expected flips - negative memory: {expected_negative / different_output_negative * 100:.1f}%")
            print(f"Proportion of unexpected flips - negative memory: {unexpected_negative / different_output_negative * 100:.1f}%\n")
        else:
            print("No flips - negative memory\n")

        if (different_output_positive + different_output_negative) != 0:
            print(f"Flip rate - TOTAL: {(different_output_positive + different_output_negative) / (different_output_positive + different_output_negative + same_output_positive + same_output_negative) * 100:.1f}%")
            print(f"Proportion of expected flips - TOTAL: {(expected_negative + expected_positive) / (different_output_positive + different_output_negative) * 100:.1f}%")
            print(f"Proportion of unexpected flips - TOTAL: {(unexpected_negative + unexpected_positive) / (different_output_positive + different_output_negative) * 100:.1f}%\n")
        else:
            print("No flips - TOTAL\n")
            

