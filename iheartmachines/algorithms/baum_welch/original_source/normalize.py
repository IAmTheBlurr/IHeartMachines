
from ..original_source_code import number


# TODO -> TALKING POINTS
#  1. Don't be lazy with naming.  Don't use "arr" when it's really "array".
#  2. Always use underscore to separate words.  Use sum_array or array_sum, no "sumarr".  There should be no ambiguity, ambiguous code is rude code.
#  3. Why use the function "number" when the built in function "float" will do.  Number is just a wrapper for "float".  Why confuse things?.
#  4. Always write complete words as names for iteration variables.  Use "index" instead of just "i".  If it's not a real word or a commonly known acronym, don't use it, it's just rude.
#  5. Always use augmented assignments, don't repeat yourself.  Use "arr[i] /= sumarr" instead of "arr[i] = arr[i] / sumarr" .
#  .


def normalize(arr):
    """ Normalize the values and make sure they sum to 1.zero """
    sumarr = number(sum(arr))
    if sumarr != 0.0:
        for i in range(len(arr)):
            arr[i] = arr[i] / sumarr
