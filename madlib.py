print "Welcome to Mad Libs"
print "Pick a Story"
print "1. Albert Einstein"
print "2. Easter"
print "3. Farm"
num = input("Enter 1 , 2 or 3: ")

if num == 1:
    print "Welcome to the Albert Einstein Story"
    place = raw_input("Enter a place: ")
    adj1 = raw_input("Enter an adjective: ")
    adj2 = raw_input("Enter another adjective: ")
    femceleb = raw_input("Enter a female celebrity: ")
    maleceleb = raw_input("Enter a male celebrity: ")
    noun1 = raw_input("Enter a noun: ")
    noun2 = raw_input("Enter another noun: ")
    noun3 = raw_input("Enter another noun: ")
    pnoun1 = raw_input("Enter a plural noun: ")
    pnoun2 = raw_input("Enter another plural noun: ")
    pnoun3 = raw_input("Enter another plural noun: ")
    pnoun4 = raw_input("Enter another plural noun: ")
    pluprof = raw_input("Enter a plural profession: ")

madlib1 = "Albert Einstein, the son of %s and %s, was born in Ulm, Germany, in 1879. In 1902, " \
              "he had a job as assistant %s in the Swiss patent office and attended the University of Zurich. There " \
              "he began studying atoms, molecules, and %s. He developed the theory of %s relativity, which expanded " \
              "the phenomena of sub-atomic %s and %s magnetism. In 1921, he won the Nobel prize for %s " \
              "and was director of theoretical physics at the Kaiser Wilhelm %s in Berlin. In 1933, when Hitler became " \
              "Chancellor of %s, Einstein came to America to take a post at Princeton Institute for %s, where his theories " \
              "helped America devise the first atomic %s. There is no question about it: Einstein was one of the most brilliant " \
              "%s of our time." % (maleceleb, femceleb, noun1, pnoun1, adj1, pnoun2, adj2, pnoun3, noun2, place, pnoun4, noun3, pluprof)
print " "
print madlib1