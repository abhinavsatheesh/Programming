using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PasswordGenerator
{
    public partial class Form1 : Form
    {
        public Form1()
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

        private void Form1_Load(object sender, EventArgs e)
        {
            GeneratePassword();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            GeneratePassword();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string gettext = label3.Text;
            string FinalToCopy = gettext.Replace("Your new password is ", "");
            System.Windows.Forms.Clipboard.SetText(FinalToCopy);
            MessageBox.Show("Password copied successfully");
        }
    }
}
