using System;

namespace Hallo {

    class Programm1 { 
        public static void Main(string[] args)
        {
            bool PrüfBool = false;

            while (PrüfBool != true)
            {
                Console.WriteLine("Geben sie die erste Zahl ein:");
                double Zahl1 = double.Parse(Console.ReadLine());

                Console.WriteLine("\nGeben sie die zweite Zahl ein:");
                double Zahl2 = double.Parse(Console.ReadLine());

                Console.WriteLine("\n\nMit welchen Operator wollen sie rechnen?");
                Console.WriteLine("+ \t - \t /\n* \t %");

                string Rechenoperator = Console.ReadLine();
                switch (Rechenoperator)
                {
                    case "+":
                        Console.WriteLine(Zahl1 + Zahl2);
                        break;
                    case "-":
                        Console.WriteLine(Zahl1 - Zahl2);
                        break;
                    case "/":
                        Console.WriteLine(Zahl1 / Zahl2);
                        break;
                    case "*":
                        Console.WriteLine(Zahl1 * Zahl2);
                        break;
                    case "%":
                        Console.WriteLine(Zahl1 % Zahl2);
                        break;
                    default:
                        Console.WriteLine("ERROR: Ein Fehler ist aufgetreten!\n\n\n");
                        break;
                PrüfBool = true;
                }

            }

        }
    }

}