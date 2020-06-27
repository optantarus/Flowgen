/*
* test file with complex combination of constructs
* If in main not shown.-> no error, function call in if currently not implemented 
* TODO: Add support for function call in if
* 
* TODO: Condition of while loop not completly shown.
* If conditions in maincycle not shown if not annotated.
* -> only last character was missing -> fixed same as for if (string_condition = string_condition[:-1])
* Loop in readInputs not shown.
* -> OK, its shown only in the level corresponding to annotations in the loop
* TODO: Build db does not add readCAN to flowdb -> because no level 0 annotation ? -> add warning.
* TODO: No end/stop node if there's not return
* TODO: No need to loop through findfunction for function declarations (see https://stackoverflow.com/questions/38295521/how-to-distinguish-function-definitions-and-function-declarations-in-clang-ast-v for solution)
* 
* INFO: annotation at line end needs a corresponding action (as for maincycle() call in main())
*/

bool init(void);
void maincycle(void);
void readInputs(void);
void readCAN(void);

int main()
{
    //$ [init successfull ?]
    if(init())
    {
        //$ call maincycle
        maincycle(); //$
    }
    else
    {
        //$ do nothing
    }
    
    return;
}

bool init(void)
{
    //$ initialize soft- and hardware
}


void maincycle(void)
{
    int timer, oldTimer, error;

	//$
    while (true)
    {
        //$ [time for new main cycle ieteration ?]
        if(timer > 10)
        {
            //$ execute main cycle
            
            //$1 read inputs
            readInputs();  //$
            
            //$1 receive can messages
            readCAN();
        }
        else if (error = 0)
        {
            //$ increment timer
            timer = timer + 1;
            
            if(timer < oldTimer)
            {
                //$ fatal error
            }
            else
            {
                //$ no problem
            }
        }
        else if (error = 1)
        {
            //$ do crazy stuff
        }
        else
        {
            //$ everything is lost
        }
    }
    
    return;
}


void readInputs()
{
    int i=0;
    
    //$ Loop through all inputs.
    for(i=0; i<10; i=i+1)
    {
        //$1 read current input value
        //$1 save value
    }
}


void readCAN()
{
    int i=0;
    int CrcReceived, CrcExpected, MsgCtrReceived, MsgCtrExpected;
    bool messageReceived;
    
    //$ [Message received ?]
    if{messageReceived == true)
    {
        //$1 store contents temporary
        
        //$1 check contents
        //$ [CRC valid ?]
        if(CrcReceived == CrcExpected)
        {
            //$2 valid CRC received 
            //$ [message counter correct]
            if(MsgCtrReceived == MsgCtrExpected)
            {
                //$2 valid message counter received
                
                //$2 store message data
            }
            else
            {
                //$2 no valid message counter received
            }
        }
        else
        {
            //$2 no valid CRC received
        }
    }
}
  
        
