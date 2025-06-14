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
    public partial class Form1 : Form
    {
        private int rectWidth;
        private int rectHeight;
        private Color rectColor;
        private bool canPaint = false;
        public Form1()
        {
            InitializeComponent();
        }

        private void quitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void sizeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SizeForm sizeForm = new SizeForm();
            if (sizeForm.ShowDialog() == DialogResult.OK)
            {
                // Получите значения размера и цвета из SizeColorForm
                rectWidth = sizeForm.RectangleWidth;
                rectHeight = sizeForm.RectangleHeight;
                rectColor = sizeForm.SelectedColor;

                // Включите функцию Paint.
                canPaint = true;
                paintToolStripMenuItem.Enabled = true;
            }
        }
        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);

            if (canPaint)
            {
                // Проверьте размер
                if (rectWidth > this.ClientSize.Width || rectHeight > this.ClientSize.Height)
                {
                    MessageBox.Show("Размер прямоугольника превышает размер окна.");
                    return;
                }

                using (Brush brush = new SolidBrush(rectColor))
                {
                    e.Graphics.FillRectangle(brush, 10, 10, rectWidth, rectHeight);
                }
            }
        }
        private void paintToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (canPaint)
            {
                this.Invalidate(); // Request Form redraw
            }
            else
            {
                MessageBox.Show("Пожалуйста, выберите размер и цвет перед покраской.");
            }
        }

        private void colorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (ColorDialog colorDialog = new ColorDialog())
            {
                if (colorDialog.ShowDialog() == DialogResult.OK)
                {
                    rectColor = colorDialog.Color;

                    if (canPaint)
                    {
                        this.Invalidate(); // Redraw the Form to apply the new color.
                    }
                }
            }
        }
    }
}
