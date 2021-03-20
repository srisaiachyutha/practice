using System;
using System.Collections.Generic;

namespace temp
{
    public enum OffOrOn
    {
        ON = 1,
        OFF = 2
    };

    abstract class Appliance
    {   
        protected int _count;
        protected OffOrOn  _state;


        public Appliance()
        {
            Count = 0;
            State = OffOrOn.OFF;
        }
        public int Count
        {
            get { return _count; }
            set { _count = value; }
        }
        public OffOrOn State
        {
            get { return _state; }
            set { _state = value; }
        }
        public string GiveState()
        {
            if (State == OffOrOn.ON)
            {
                return "On";
            }
            else
            {
                return "Off";
            }
        }
        public void ModifyState(int state) {
            if(state == 1)
            {
                State = OffOrOn.ON;
            }
            if(state == 0)
            {
                State = OffOrOn.OFF;
            }

        }
        public void ToggleState()
        {
            if(State == OffOrOn.ON)
            {
                State = OffOrOn.OFF;
            }
            else
            {
                State = OffOrOn.ON;
            }
        }
        public abstract void GetStatus();
        public abstract string ReturnClassName();
        public abstract string CurrentNumer();

    }

    class Fan : Appliance 
    {
        public int currentNumber;
        public override string ReturnClassName()
        {
            return this.GetType().Name;
        }
        
        public override string CurrentNumer()
        {
            return currentNumber.ToString();
        }

        public override void GetStatus()
        {
            Console.WriteLine(this.GetType().Name  + currentNumber.ToString() + " is " + GiveState() );
        }
        public Fan(int value = 0)
        {
            this.currentNumber = value;
        }
        
    }
    class Ac : Appliance
    {
        public int currentNumber;
        public override string ReturnClassName()
        {
            return this.GetType().Name;

        }
        public override string CurrentNumer()
        {
            return currentNumber.ToString();
        }
        public override void GetStatus()
        {
            Console.WriteLine(this.GetType().Name + currentNumber.ToString() + " is " + GiveState());
        }
        public Ac(int value = 0)
        {
            this.currentNumber = value;
        }

    }
    class Bulb : Appliance
    {
        public int currentNumber;
        public override string ReturnClassName()
        {
            return this.GetType().Name;
        }
        public override string CurrentNumer()
        {
            return currentNumber.ToString();
        }
        public override void GetStatus()
        {
            Console.WriteLine(this.GetType().Name + currentNumber.ToString() + " is " + GiveState());
        }
        public Bulb(int value = 0)
        {
            this.currentNumber = value;
        }

    }

    class SwitchBoard
    {
        public static bool IsNegative( int value)
        {
            return value < 0;
        }

        public static void Menu(ref List<Appliance> devices) {
            int count = 1;
            foreach (var device in devices)
            {
                Console.Write(count.ToString()+" ");
                device.GetStatus();
                count++;
            }
        }

        static void Main(string[] args)
        {
            List<Appliance> devices = new List<Appliance>();
            bool mainLoopCondition = true;
            int fans , acs , bulbs;
          
            Console.WriteLine("Enter the number of fans");
            fans = Convert.ToInt32(Console.ReadLine());
            for(int i = 0; i< fans; i++)
            {
                devices.Add(new Fan(i + 1));
            }
            Console.WriteLine("Enter the number of acs");
            acs = Convert.ToInt32(Console.ReadLine());
            for (int i = 0; i < acs; i++)
            {
                devices.Add(new Ac(i + 1));
            }
            Console.WriteLine("Enter the number of bulbs");
            bulbs = Convert.ToInt32(Console.ReadLine());
            for (int i = 0; i < bulbs; i++)
            {
                devices.Add(new Bulb(i + 1));
            }
            while (mainLoopCondition)
            {
                Menu(ref devices);
                Console.WriteLine("enter a number");
                int temp = Convert.ToInt32(Console.ReadLine()) -1;
                int choice;
                while (true)
                {
                    Console.WriteLine("1. Switch  " + devices[temp].ReturnClassName()+ devices[temp].CurrentNumer()+" " + devices[temp].GiveState() + "\n2. Back\n" );

                    choice = Convert.ToInt32(Console.ReadLine());
                    if(choice == 1)
                    {
                        devices[temp].ToggleState();
                        break;
                    }
                    else if(choice ==2)
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Enter a valid menu option");
                    }

                }
                Console.WriteLine("Enter y (or) n to continue (or) discontinue");
                if(Convert.ToString(Console.ReadLine()) == "n")
                {
                    mainLoopCondition = false;
                }
                
            }

       
            Console.ReadKey();
        }
    }
}
