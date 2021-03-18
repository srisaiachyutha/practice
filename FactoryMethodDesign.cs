using System;

namespace Factory
{
    /// <summary>
    /// product
    /// </summary>
    public interface IVehicle
    {
       int MaxDriveSpeed();
        void ModifySpeed(int speed);

    }

    /// <summary>
    /// a Concrete product : Bike class
    /// </summary>
    public class Bike : IVehicle
    {
        private int _speed;
        public Bike(int speed)
        {
            this._speed = speed;

        }
       public int MaxDriveSpeed() {

            return this._speed;
        }
        public void ModifySpeed(int speed)

        {
            this._speed = speed;
        }
    }
    /// <summary>
    /// a Concrete product : Car class
    /// </summary>
    public class Car : IVehicle
    {
        private int _speed;
        public Car(int speed)
        {
            this._speed = speed;

        }
        public int MaxDriveSpeed()
        {

            return this._speed;

        }
        public void ModifySpeed(int speed)

        {
            this._speed = speed;
        }
    }
    /// <summary>
    /// a Concrete product : Car class
    /// </summary>
    public class Ship : IVehicle
    {
        private int _speed;
        public Ship(int speed)
        {
            this._speed = speed;

        }
        public int MaxDriveSpeed()
        {

            return this._speed;
        }
        public void ModifySpeed(int speed)

        {
            this._speed = speed;
        }

    }
    /// <summary>
    /// Creator
    /// </summary>
    public abstract class VehicleFactory
    {
       public abstract IVehicle GetVehicle(string vehicleType);
    }

    public class ConcreteVehicleFactory : VehicleFactory
    {
        public override IVehicle GetVehicle(string vehicleType)
        {
            switch (vehicleType)
            {
                case "Car":
                    return new Car(200);
                case "Bike":
                    return new Bike(100);
                case "Ship":
                    return new Ship(180);
                default:
                    throw new ApplicationException();
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            VehicleFactory factory = new ConcreteVehicleFactory();
            IVehicle car = factory.GetVehicle("Car");
            Console.WriteLine($"the maximum speed of car is "+car.MaxDriveSpeed().ToString());

            car.ModifySpeed(280);
            Console.WriteLine("after modification the maximum speed of car is " + car.MaxDriveSpeed().ToString());

            Console.ReadKey();
                 
        }
    }
}
