def predict_the_winner(self, nums):
    def can_p1_win(nums, p1_score, p2_score, is_p1_turn):
        if len(nums) == 0:
            return p1_score >= p2_score
        
        first_element = nums[0]
        last_element = nums[-1]
        if is_p1_turn:
            return can_p1_win(
                nums[1:],
                p1_score + first_element,
                p2_score,
                False
            ) or can_p1_win(
                nums[:-1],
                p1_score + last_element,
                p2_score,
                False
            )
        else:
            return can_p1_win(
                nums[1:],
                p1_score,
                p2_score + first_element,
                True
            ) and can_p1_win(
                nums[:-1],
                p1_score,
                p2_score + + last_element,
                True
            )

    return can_p1_win(nums, 0, 0, True)