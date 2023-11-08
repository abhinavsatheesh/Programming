using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace PasswordGenerator
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }
        private void GeneratePassword()
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
            label3.Text = "Your new password is " + FinalPassword;
        }
        private void Window1_Load(object sender, EventArgs e)
        {
            GeneratePassword();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            GeneratePassword();
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            string gettext = label3.Text;
            string FinalToCopy = gettext.Replace("Your new password is ", "");
            Clipboard.SetText(FinalToCopy);
            MessageBox.Show("Password copied successfully");
        }
    }
}
