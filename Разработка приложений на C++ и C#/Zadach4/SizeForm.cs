using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Zadach4
{
    public partial class SizeForm : Form
    {
        public int RectangleWidth { get; private set; }
        public int RectangleHeight { get; private set; }
        public Color SelectedColor { get; private set; }
        public SizeForm()
        {
            InitializeComponent();
            SelectedColor = Color.Black;
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
        private void colorButton_Click(object sender, EventArgs e)
        {
            using (ColorDialog colorDialog = new ColorDialog())
            {
                if (colorDialog.ShowDialog() == DialogResult.OK)
                {
                    SelectedColor = colorDialog.Color; // Запишите выбранный цвет
                }
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            if (int.TryParse(textBox1.Text, out int width) && int.TryParse(textBox2.Text, out int height))
            {
                RectangleWidth = width;
                RectangleHeight = height;
                this.DialogResult = DialogResult.OK;
                this.Close();
            }
            else
            {
                MessageBox.Show("Введите действительный размер прямоугольника.");
            }
        }
    }
}