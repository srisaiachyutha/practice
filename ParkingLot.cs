using System;
using System.Collections.Generic;
namespace parking
{
    public enum VehicleType
    {
        TWO = 1,
        FOUR = 2,
        HEAVY = 4

    };
    public class Ticket
    {
        private VehicleType _type;
        private int _vehicleNumber;
        private int _slotNumber;
        private DateTime _inTime;
        private DateTime? _outTime;
        public Ticket(int vehicleNumber,
                      int slotNumber,
                      VehicleType v,
                      DateTime inTime,
                      DateTime? outTime = null
                      )
        {
            this._inTime = inTime;
            this._outTime = outTime;
            this._slotNumber = slotNumber;
            this._vehicleNumber = vehicleNumber;
            this._type = v;

        }
        public int SlotNumber()
        {
            return this._slotNumber;
        }
        public VehicleType TypeofVehicle()
        {
            return this._type;
        }
        public int NumberPlate()
        {
            return this._vehicleNumber;
        }

    }

    public class ParkingLot
    {
        private Dictionary<string, Ticket> _dict = new Dictionary<string, Ticket>();
        private int _twoWheelers;
        private int _fourWheelers;
        private int _heavyVehicles;
        public int TwoWheelers
        {
            get { return this._twoWheelers; }
            set { this._twoWheelers = value; }
        }
        public int FourWheelers
        {
            get { return this._fourWheelers; }
            set { this._fourWheelers = value; }
        }
        public int HeavyVehicles
        {
            get { return this._heavyVehicles; }
            set { this._heavyVehicles = value; }
        }

        public void AddVehicleNumber(int vehicleNumber, VehicleType v)
        {
            Random r = new Random();
            int n;
            do
            {
                n = r.Next(1, 1000);
            } while (this._dict.ContainsKey(n.ToString()));

            this._dict.Add(vehicleNumber.ToString(), new Ticket(vehicleNumber, n, v, DateTime.Now));


        }

        public bool RemoveVehicle(int vehicle)
        {
            if (this._dict.ContainsKey(vehicle.ToString()))
            {
                Ticket t = this._dict[vehicle.ToString()];
                switch (t.TypeofVehicle())
                {
                    case VehicleType.TWO:
                        this._twoWheelers += 1;
                        break;
                    case VehicleType.FOUR:
                        this._fourWheelers += 1;
                        break;
                    case VehicleType.HEAVY:
                        this._heavyVehicles += 1;
                        break;
                }
                this._dict.Remove(vehicle.ToString());
                return true;
            }
            return false;
        }

        public void ShowDetails()
        {
            Console.WriteLine("there are " + this._twoWheelers.ToString() +
            "two wheeler empty slots" + this._fourWheelers.ToString() +
            "Four wheeler empty slots" + this._heavyVehicles.ToString() +
            "heavy vehicles"
            );
            foreach (KeyValuePair<string, Ticket> item in this._dict)
            {
                Console.WriteLine(@"slot number: {0} vehicle number: {1} ", item.Value.SlotNumber().ToString(), item.Value.NumberPlate());
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            ParkingLot p = new ParkingLot();

            Console.WriteLine("Enter the 2 wheeler parking count");
            p.TwoWheelers = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter the 4 wheeler parking count");
            p.FourWheelers = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter the heavy vehicles parking count");
            p.HeavyVehicles = Convert.ToInt32(Console.ReadLine());

            while (true)
            {
                Console.WriteLine("1. See parking details\n2.Park Vehicle\n3.Unpark Vehicle");
                int choice = Convert.ToInt32(Console.ReadLine());
                switch (choice)
                {
                    case 1:
                        // parking details
                        p.ShowDetails();
                        break;
                    case 2:
                        // park vehicle
                        Console.WriteLine("choose the options below");
                        Console.WriteLine("1. two Wheeler\n2. four wheeler \n3. heavy vehicles");
                        int parkChoice = Convert.ToInt32(Console.ReadLine());
                        Console.WriteLine("enter the vehicle number");
                        int vehicle = Convert.ToInt32(Console.ReadLine());

                        switch (parkChoice)
                        {
                            case 1:
                                if (p.TwoWheelers > 0)
                                {
                                    p.TwoWheelers -= 1;
                                    p.AddVehicleNumber(vehicle, VehicleType.TWO);
                                    Console.WriteLine("the vehicle has parked successfully");
                                }
                                else
                                {
                                    Console.WriteLine(" the slots are not empty ");
                                }
                                break;
                            case 2:
                                if (p.FourWheelers > 0)
                                {
                                    p.FourWheelers -= 1;
                                    p.AddVehicleNumber(vehicle, VehicleType.FOUR);
                                    Console.WriteLine("the vehicle has parked successfully");

                                }
                                else
                                {
                                    Console.WriteLine(" the slots are not empty ");
                                }
                                break;
                            case 3:
                                if (p.HeavyVehicles > 0)
                                {
                                    p.HeavyVehicles -= 1;
                                    p.AddVehicleNumber(vehicle, VehicleType.HEAVY);
                                    Console.WriteLine("the vehicle has parked successfully");

                                }
                                else
                                {
                                    Console.WriteLine(" the slots are not empty ");
                                }
                                break;
                        }
                        break;

                    case 3:
                        // Unpark vehicle
                        Console.WriteLine("enter the vehicle number");
                        int v = Convert.ToInt32(Console.ReadLine());
                        if (p.RemoveVehicle(v))
                        {
                            Console.WriteLine("the vehicle is removed from park lot");
                        }
                        break;
                    default:
                        // choose a good number
                        Console.WriteLine("please choose the number from menu");
                        break;
                }

                Console.WriteLine("y (or) n for continue  (or) exit");
                if (Console.ReadLine() == "n")
                {
                    break;
                }
            }
        }
    }
}
