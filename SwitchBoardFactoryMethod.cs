using System;
using System.Collections.Generic;
namespace SwitchBorad
{
    public enum OffOrOn
    {
        ON = 1,
        OFF = 2
    };
    /// <summary>
    /// product interface : device interface
    /// </summary>
    public interface IDevice
    {
        public string GiveState();
        public void ModifyState(int state);
        public void ToggleState();
        public abstract void GetStatus();
        public abstract string ReturnClassName();
        public abstract string CurrentNumer();
    }

    /// <summary>
    /// concreate product : Fan class
    /// </summary>
    class Fan : IDevice
    {
        private int _currentNo;
        private OffOrOn _state = OffOrOn.OFF;
        public Fan(int count) {
            this._currentNo = count;
        }
        public string GiveState()
        {
            if (this._state == OffOrOn.ON)
            {
                return "On";
            }
            else
            {
                return "Off";
            }
        }
        public void ModifyState(int state)
        {
            if (state == 1)
            {
                this._state = OffOrOn.ON;
            }
            if (state == 0)
            {
                this._state = OffOrOn.OFF;
            }

        }
        public void ToggleState()
        {
            if (this._state == OffOrOn.ON)
            {
                this._state = OffOrOn.OFF;
            }
            else
            {
                this._state = OffOrOn.ON;
            }
        }
        public  void GetStatus()
        {
            Console.WriteLine(this.GetType().Name+" " + CurrentNumer() + " is " + GiveState());
        }
        public  string ReturnClassName()
        {
            return this.GetType().Name;
        }
        public  string CurrentNumer()
        {
            return this._currentNo.ToString();
        }
    }

    /// <summary>
    /// concrete product : Ac class
    /// </summary>
    class Ac : IDevice
    {
        private int _currentNo;
        private OffOrOn _state = OffOrOn.OFF;
        public Ac(int count)
        {
            this._currentNo = count;
        }
        public string GiveState()
        {
            if (this._state == OffOrOn.ON)
            {
                return "On";
            }
            else
            {
                return "Off";
            }
        }
        public void ModifyState(int state)
        {
            if (state == 1)
            {
                this._state = OffOrOn.ON;
            }
            if (state == 0)
            {
                this._state = OffOrOn.OFF;
            }

        }
        public void ToggleState()
        {
            if (this._state == OffOrOn.ON)
            {
                this._state = OffOrOn.OFF;
            }
            else
            {
                this._state = OffOrOn.ON;
            }
        }
        public void GetStatus()
        {
            Console.WriteLine(this.GetType().Name + " " + CurrentNumer() + " is " + GiveState());
        }
        public string ReturnClassName()
        {
            return this.GetType().Name;
        }
        public string CurrentNumer()
        {
            return this._currentNo.ToString();
        }
    }

    /// <summary>
    /// concrete product : bulb class
    /// </summary>
    class Bulb : IDevice
    {
        private int _currentNo;
        private OffOrOn _state = OffOrOn.OFF;
        public Bulb(int count)
        {
            this._currentNo = count;
        }
        public string GiveState()
        {
            if (this._state == OffOrOn.ON)
            {
                return "On";
            }
            else
            {
                return "Off";
            }
        }
        public void ModifyState(int state)
        {
            if (state == 1)
            {
                this._state = OffOrOn.ON;
            }
            if (state == 0)
            {
                this._state = OffOrOn.OFF;
            }

        }
        public void ToggleState()
        {
            if (this._state == OffOrOn.ON)
            {
                this._state = OffOrOn.OFF;
            }
            else
            {
                this._state = OffOrOn.ON;
            }
        }
        public void GetStatus()
        {
            Console.WriteLine(this.GetType().Name + " " + CurrentNumer() + " is " + GiveState());
        }
        public string ReturnClassName()
        {
            return this.GetType().Name;
        }
        public string CurrentNumer()
        {
            return this._currentNo.ToString();
        }
    }

    /// <summary>
    /// creator
    /// </summary>
    public abstract class DeviceFactory
    {
        public abstract IDevice GetDevice(string deviceType , int count);
    }

    /// <summary>
    /// concrete creator 
    /// </summary>
    public class ConcreteDeviceFactory : DeviceFactory
    {
        public override IDevice GetDevice(string deviceType , int count)
        {
            switch (deviceType)
            {
                case "Ac":
                    return new Ac(count);
                case "Bulb":
                    return new Bulb(count);
                case "Fan":
                    return new Fan(count);
                default:
                    throw new ApplicationException();
            }
        }
    }
    class Program
    {
        public static bool IsNegative(int value)
        {
            return value < 0;
        }

        public static void Menu(ref List<IDevice> devices)
        {
            int count = 1;
            foreach (var device in devices)
            {
                Console.Write(count.ToString() + " ");
                device.GetStatus();
                count++;
            }
        }

        static void Main(string[] args)
        {
            DeviceFactory factory = new ConcreteDeviceFactory();
            List<IDevice> devices = new List<IDevice>();
            bool mainLoopCondition = true;
            int fans, acs, bulbs;

            Console.WriteLine("Enter the number of fans");
            fans = Convert.ToInt32(Console.ReadLine());
            for (int i = 0; i < fans; i++)
            {
                devices.Add(factory.GetDevice("Fan" , i));
            }
            Console.WriteLine("Enter the number of acs");
            acs = Convert.ToInt32(Console.ReadLine());
            for (int i = 0; i < acs; i++)
            {
                devices.Add(factory.GetDevice("Ac", i));
            }
            Console.WriteLine("Enter the number of bulbs");
            bulbs = Convert.ToInt32(Console.ReadLine());
            for (int i = 0; i < bulbs; i++)
            {
                devices.Add(factory.GetDevice("Bulb", i));
            }

            while (mainLoopCondition)
            {
                Menu(ref devices);
                Console.WriteLine("enter a number");
                int temp = Convert.ToInt32(Console.ReadLine()) - 1;
                int choice;
                while (true)
                {
                    Console.WriteLine("1. Switch  " + devices[temp].ReturnClassName() + devices[temp].CurrentNumer() + " " + devices[temp].GiveState() + "\n2. Back\n");

                    choice = Convert.ToInt32(Console.ReadLine());
                    if (choice == 1)
                    {
                        devices[temp].ToggleState();
                        break;
                    }
                    else if (choice == 2)
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Enter a valid menu option");
                    }

                }
                Console.WriteLine("Enter y (or) n to continue (or) discontinue");
                if (Convert.ToString(Console.ReadLine()) == "n")
                {
                    mainLoopCondition = false;
                    Menu(ref devices);
                    Console.WriteLine(" the switch board application is terminated");
                }

            }


            Console.ReadKey();
        }
    }
}
