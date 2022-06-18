using System;

namespace PasswordGenerator
{
    class Program
    {
        static void GeneratePassword()
        {
            var random = new Random();
            var AdjectivesList = new List<string> {"enormous", "doglike", "silly", "yellow", "fun", "fast", "beautiful", "sleepy", "slow", "smelly", "wet", "fat", "red", "orange", "yellow", "green",
"blue", "purple", "fluffy", "white", "proud", "brave", "adorable", "amused", "annoying", "ashamed", "awful", "better", "bloody", "blushing", "brave", "busy" };
            var NounList = new List<string> { "apple", "dinosaur", "ball", "toaster", "goat", "dragon", "hammer", "duck", "panda", "more", "some ", "telephone", "banana", "teacher" };
            var SpecialChar = new List<string> { "@", "!", "#", "^", "&", "*", "(", ")", "$", "-", "=", "/" };
            int randAdjectives = random.Next(AdjectivesList.Count);
            int randNoun = random.Next(NounList.Count);
            int randNum = random.Next(0, 100);
            int randSpecialChar = random.Next(SpecialChar.Count);
            string FinalAdjective = AdjectivesList[randAdjectives];
            string FinalNoun = NounList[randNoun];
            string FinalNum = Convert.ToString(randNum);
            string FinalSpecialChar = SpecialChar[randSpecialChar];
            string FinalPassword = FinalAdjective + FinalNoun + FinalNum + FinalSpecialChar;
            Console.WriteLine("Your new password is " + FinalPassword);
        }
        static void debug(String data)
        {
            Console.WriteLine(data);
        }
        static void Main(String[] args)
        {
            
            Console.WriteLine("Hi. Welcome to Password Picker");
            GeneratePassword();
            while (true) {
                Console.WriteLine("Do you need another password? Type Y or N");
                string option = Console.ReadLine();
                if (option == "Y")
                {
                    Console.WriteLine("Ok");
                    GeneratePassword();
                }
                else
                {
                    Console.WriteLine("Ok");
                    Environment.Exit(0);
                }
            }
            
        }
    }
}