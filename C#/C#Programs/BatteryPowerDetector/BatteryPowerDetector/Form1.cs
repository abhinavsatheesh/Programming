using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BatteryPowerDetector
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void GetBattery()
        {
            PowerStatus status = SystemInformation.PowerStatus;
            string batterylevel = status.BatteryLifePercent.ToString("P0");
            label2.Text = "Battery Level : " + batterylevel;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            backgroundWorker1.RunWorkerAsync();
        }

        private void backgroundWorker1_DoWork(object sender, System.ComponentModel.DoWorkEventArgs e)
        {
            while (true)
            {
                GetBattery();
            }
        }
    }
}
