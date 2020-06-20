// test file with complex combination of constructs
// TODO: If in main not shown.
// TODO: Condition of while loop not completly shown.
// TODO: If conditions un maincycle not shown if not annotated.
// TODO: Loop in readInputs not shown.

bool init(void);
void maincycle(void);
void readInputs(void);
void readCAN(void);

int main()
{
    //$ [init successfull ?]
    if(init()) //$
    {
        maincycle(); //$
    }
    else
    {
        //$ do nothing
    }
    
    return;
}

init()
{
    //$ initialize soft- and hardware
}


maincycle()
{
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
    init i=0;
    
    //$ Loop through all inputs.
    for(i=0; i<10; i=i+1)
    {
        //$1 read current input value
        //$1 save value
    }
}


void readCAN()
{
    init i=0;
    
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
  
        
