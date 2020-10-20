import textdistance as td

def levenshtein_accuracy(input, output, token):
    if(token == True):
        gap = len(output)-len(input)
        if(gap == 0):
            sum = 0
            for i in range(len(input)):
                sum += td.levenshtein(input[i],output[i])
            accuracy = sum/len(input)

        elif(gap < 0):  #output less tokens than input, original > generated
            i = 0
            j = 0
            gap = abs(gap)
            tokens = [0]*gap
        else:           #output more tokens than input, original < generated
            i = 0
            j = 0
            
    else:
        input_string = ' '.join(input)
        output_string = ' '.join(output)
        print(input_string)
        print(output_string)

        accuracy = td.levenshtein.normalized_similarity(input_string, output_string)

    return accuracy
        
