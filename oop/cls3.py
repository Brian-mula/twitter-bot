

# structured analysis is an approach to analysisi and design software systems.
# within this area there are many specific and well documented methods including SSADM(structured system analysis and design method)
# and Yourden method.
# ?however, we'll forcus on one specific approach and we'll outline the key ideas and the 2 basic elements for more structure analysis methods:
# i.e functional decomposition and data flow analysis,
# we'll also look at flow chats for designing algorythims

#               STRUCTURED ANALYSIS AND FUNCTIONAL IDENTIFICATION
# the struictured analysis methods typically employs a process driven approach which in one way or another considers wat the input and output of the systems are and how those inputs are transformed into outputs
# this transformation involves the application of one or more functions
# the steps involved here identify these functions and wil typically iteratively break them down into smaller funtions until an appropriate levels of details has been reached
# this process is known as funtional decomposition
# although simple py programs may only contain a syquence of statements and expressions,any program of a significant size will need to be structured such that it can be
#               1. understood easily by other devs
            # 2 tested to ensure thatr it does what it intends
            #   maintained as new and existing requirements evolve
            #   debug to resolve unexpected or undesirable behavior
    # funtional decomposition supports the analysis and identification of these functions


    # FUNTIONAL DECOMPOSITION
    # in one way in which a sytem can be broken down into its constituent parts
    # e.g for a comp payroll system to calcuate how much an hourly paid employee should recieve,it might be necessary to"
    #           load employees details from some form of permanent storage
    #            load how many hours the employee has worked for the week
    #           multip[ly the hours worked by the employee's hourly rate
    # /           record how much the employee is to be paid in a payroll database or file
    #           print out the employees' payslip
    #           transfer the appropriate funds to the employees's bank account
    #           record in the payroll db that everything has been completed


    # NOTE: each of the above steps could represent a function performed by the system

    # this process of breaking down higher level func into low level func will help with:
    #           1. testing the system
    #           2. understanding the system as the organization of the func can bring meaning to the code.
    #           as well as allowing each func to be understood in isolation from the rest of the system
    #           3. maintaining the system as only those func that need to be changed maybe affected by new or modified requirements
    #           4. debugging the sytem as issues can be isolated by specific funcs which cn be examined independently of the rest of the application

    # note: it is also known as top=down refinement appproach.
    #  the term top-down refinement highlights the idea that we're breaking down a system into the sub systems that makes it up
    # 