namespace NotificationWindows
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string AppName = textBox1.Text;
            string Text = richTextBox1.Text;
            int Seconds = Convert.ToInt16(textBox2.Text);
            int MilliSeconds = Seconds * 1000;
            var notification = new System.Windows.Forms.NotifyIcon()
            {
                Visible = true,
                Icon = System.Drawing.SystemIcons.Information,
                
                BalloonTipTitle = AppName,
                BalloonTipText = Text,
            };
            notification.ShowBalloonTip(MilliSeconds);
            Thread.Sleep(10000);
            notification.Dispose();
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            if (System.Text.RegularExpressions.Regex.IsMatch(textBox2.Text, "[^0-9]"))
            {
                textBox2.Text = textBox2.Text.Remove(textBox2.Text.Length - 1);
            }
        }
    }
}