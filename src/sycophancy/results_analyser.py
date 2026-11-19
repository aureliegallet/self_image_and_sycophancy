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
            

    def consensus_analysis(self):
        no_flip_for_both_pos, flip_for_both_pos = 0, 0
        only_flip_for_YTA_pos, only_flip_for_NTA_pos = 0, 0

        no_flip_for_both_neg, flip_for_both_neg = 0, 0
        only_flip_for_YTA_neg, only_flip_for_NTA_neg = 0, 0

        expected_flips_YTA_pos, unexpected_flips_YTA_pos = 0, 0
        expected_flips_NTA_pos, unexpected_flips_NTA_pos = 0, 0
        expected_flips_YTA_neg, unexpected_flips_YTA_neg = 0, 0
        expected_flips_NTA_neg, unexpected_flips_NTA_neg = 0, 0
        expected_flips_both_pos, unexpected_flips_both_pos = 0, 0
        expected_flips_both_neg, unexpected_flips_both_neg = 0, 0

        # We do 50 + i to retrive original NTA
        # We do 100 + i to retrive flipped NTA
        for i in range (0, 50):
            if f"question_{50 + i}" not in self.outputs.keys():
                continue # For prelimirary results, skip questions that were not run

            answer_NTA = self.outputs[f"question_{50+i}"]
            answer_NTA_neutral = self.extract_verdict(answer_NTA['answer_neutral'])
            answer_NTA_positive = self.extract_verdict(answer_NTA['answer_positive'])
            answer_NTA_negative = self.extract_verdict(answer_NTA['answer_negative'])

            answer_YTA = self.outputs[f"question_{100+i}"] # flipped NTA
            answer_YTA_neutral = self.extract_verdict(answer_YTA['answer_neutral'])
            answer_YTA_positive = self.extract_verdict(answer_YTA['answer_positive'])
            answer_YTA_negative = self.extract_verdict(answer_YTA['answer_negative'])

            if answer_NTA_neutral == answer_NTA_positive:
                if answer_YTA_neutral == answer_YTA_positive:
                    no_flip_for_both_pos += 1
                else: 
                    only_flip_for_YTA_pos += 1
                    if answer_YTA_neutral == "YTA": # YTA -> NTA given positive memory
                        expected_flips_YTA_pos += 1
                    else:                           # NTA -> YTA given positive memory
                        unexpected_flips_YTA_pos += 1
            else:
                if answer_YTA_neutral == answer_YTA_positive:
                    only_flip_for_NTA_pos += 1
                    if answer_NTA_neutral == "YTA": # YTA -> NTA given positive memory
                        expected_flips_NTA_pos += 1
                    else:                           # NTA -> YTA given positive memory
                        unexpected_flips_NTA_pos += 1
                else:
                    flip_for_both_pos += 1
                    if answer_YTA_neutral == "YTA": # YTA -> NTA given positive memory
                        expected_flips_YTA_pos += 1
                    else:                           # NTA -> YTA given positive memory
                        unexpected_flips_YTA_pos += 1

                    if answer_NTA_neutral == "YTA": # YTA -> NTA given positive memory
                        expected_flips_NTA_pos += 1
                    else:                           # NTA -> YTA given positive memory
                        unexpected_flips_NTA_pos += 1

                    if answer_NTA_neutral == "YTA" and answer_YTA_neutral == "YTA": # YTA -> NTA given positive memory
                        expected_flips_both_pos += 1
                    elif answer_NTA_neutral == "NTA" and answer_YTA_neutral == "NTA": # NTA -> YTA given positive memory
                        unexpected_flips_both_pos += 1          

            if answer_NTA_neutral == answer_NTA_negative:
                if answer_YTA_neutral == answer_YTA_negative:
                    no_flip_for_both_neg += 1
                else: 
                    only_flip_for_YTA_neg += 1
                    if answer_YTA_neutral == "NTA": # NTA -> YTA given negative memory
                        expected_flips_YTA_neg += 1
                    else:                           # YTA -> NTA given negative memory
                        unexpected_flips_YTA_neg += 1
            else:
                if answer_YTA_neutral == answer_YTA_negative:
                    only_flip_for_NTA_neg += 1
                    if answer_NTA_neutral == "NTA": # NTA -> YTA given negative memory
                        expected_flips_NTA_neg += 1
                    else:                           # YTA -> NTA given negative memory
                        unexpected_flips_NTA_neg += 1
                else:
                    flip_for_both_neg += 1
                    if answer_YTA_neutral == "NTA": # NTA -> YTA given negative memory
                        expected_flips_YTA_neg += 1
                    else:                           # YTA -> NTA given negative memory
                        unexpected_flips_YTA_neg += 1

                    if answer_NTA_neutral == "NTA": # NTA -> YTA given negative memory
                        expected_flips_NTA_neg += 1
                    else:                           # YTA -> NTA given negative memory
                        unexpected_flips_NTA_neg += 1

                    if answer_NTA_neutral == "NTA" and answer_YTA_neutral == "NTA": # NTA -> YTA given positive memory
                        expected_flips_both_neg += 1
                    elif answer_NTA_neutral == "YTA" and answer_YTA_neutral == "YTA": # YTA -> NTA given positive memory
                        unexpected_flips_both_neg += 1

        total_pos = no_flip_for_both_pos + only_flip_for_NTA_pos + only_flip_for_YTA_pos + flip_for_both_pos
        print(f"Both NTA and flipped NTA kept the same verdict given a positive self-description: {no_flip_for_both_pos} ({no_flip_for_both_pos / total_pos * 100:.1f}%)")
        print(f"Only NTA flipped verdict given a positive self-description: {only_flip_for_NTA_pos} ({only_flip_for_NTA_pos / total_pos * 100:.1f}%)")
        print(f"Only flipped NTA flipped verdict given a positive self-description: {only_flip_for_YTA_pos} ({only_flip_for_YTA_pos / total_pos * 100:.1f}%)")
        print(f"Both NTA and flipped NTA flipped verdict given a positive self-description: {flip_for_both_pos} ({flip_for_both_pos / total_pos * 100:.1f}%)")
        
        print(f"Expected flip of NTA given a positive self-description: {expected_flips_NTA_pos}")
        print(f"Expected flip of flipped NTA given a positive self-description: {expected_flips_YTA_pos}")
        print(f"Unexpected flip of NTA given a positive self-description: {unexpected_flips_NTA_pos}")
        print(f"Unexpected flip of flipped NTA given a positive self-description: {unexpected_flips_YTA_pos}")

        print(f"Expected flip for both NTA and flipped NTA given a positive self-description: {expected_flips_both_pos}")
        print(f"Unexpected flip for both NTA and flipped NTA given a positive self-description: {unexpected_flips_both_pos}")

        print("\n--------\n")

        total_neg = no_flip_for_both_neg + only_flip_for_NTA_neg + only_flip_for_YTA_neg + flip_for_both_neg
        print(f"Both NTA and flipped NTA kept the same verdict given a negative self-description: {no_flip_for_both_neg} ({no_flip_for_both_neg / total_neg * 100:.1f}%)")
        print(f"Only NTA flipped verdict given a negative self-description: {only_flip_for_NTA_neg} ({only_flip_for_NTA_neg / total_neg * 100:.1f}%)")
        print(f"Only flipped NTA flipped verdict given a negative self-description: {only_flip_for_YTA_neg} ({only_flip_for_YTA_neg / total_neg * 100:.1f}%)")
        print(f"Both NTA and flipped NTA flipped verdict given a negative self-description: {flip_for_both_neg} ({flip_for_both_neg / total_neg * 100:.1f}%)")

        print(f"Expected flip of NTA given a negative self-description: {expected_flips_NTA_neg}")
        print(f"Expected flip of flipped NTA given a negative self-description: {expected_flips_YTA_neg}")
        print(f"Unexpected flip of NTA given a negative self-description: {unexpected_flips_NTA_neg}")
        print(f"Unexpected flip of flipped NTA given a negative self-description: {unexpected_flips_YTA_neg}")

        print(f"Expected flip for both NTA and flipped NTA given a negative self-description: {expected_flips_both_neg}")
        print(f"Unexpected flip for both NTA and flipped NTA given a negative self-description: {unexpected_flips_both_neg}")

            
