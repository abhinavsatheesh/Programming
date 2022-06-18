namespace SatheeshFinancialDoubtSolver
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Close(object sender, FormClosingEventArgs e)
        {
            Application.Exit();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            Form f2 = new Form2();
            f2.ShowDialog();
        }
        private void button2_Click(object sender, EventArgs e)
        {
            Form f4 = new Form4();
            f4.ShowDialog();
        }
        private void button3_Click(object sender, EventArgs e)
        {
            Form f3 = new Form3();
            f3.ShowDialog();
        }
    }
}