# Type Conversion:
# Write a function that prompts the user to enter a number and tries to convert it to an
# integer. Handle the TypeError exception by printing a message indicating that the input
# is not a valid number. Use a finally block to print "Type conversion process completed."

# funxtioni mej poxancelu enq string vori mej kam tiva kam tiv chi im gorcy ena vor stugem te karum em tiv sarqem tiv ksarqem ete texta mejy grac chem kara

def type_conversion(word_or_number) :
    try:      
        return int(word_or_number)
    
    except ValueError:
        raise TypeError("it is not a number")

    finally:
        print("Type conversion process completed.")

print(type_conversion("p"))        
