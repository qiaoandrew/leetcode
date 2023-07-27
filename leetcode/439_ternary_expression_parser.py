class RecursionSolution:
    def parseTernary(self, expression):
        if len(expression) == 1 or expression[1] != '?':
            return expression[0]
        
        if expression[0] == 'T':
            return self.parseTernary(expression[2:])
        
        num_question_marks = 0
        for i in range(2, len(expression)):
            if expression[i] == '?':
                num_question_marks += 1
            elif expression[i] == ':' and num_question_marks > 0:
                num_question_marks -= 1
            elif expression[i] == ':' and num_question_marks == 0:
                return self.parseTernary(expression[i + 1:])