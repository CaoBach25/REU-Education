#pragma once
#include "SizeForm.h"

namespace Zadach4c {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;

	/// <summary>
	/// Summary for MainForm
	/// </summary>
	public ref class MainForm : public System::Windows::Forms::Form
	{
	public:
		MainForm(void)
		{
			InitializeComponent();
			paintToolStripMenuItem->Enabled = false;
		}
	private:
		int rectWidth = 0;
		int rectHeight = 0;
		Color rectColor = Color::Black;

	protected:
		~MainForm()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::MenuStrip^ menuStrip1;
	private: System::Windows::Forms::ToolStripMenuItem^ sizeToolStripMenuItem;
	private: System::Windows::Forms::ToolStripMenuItem^ colorToolStripMenuItem;
	private: System::Windows::Forms::ToolStripMenuItem^ paintToolStripMenuItem;
	private: System::Windows::Forms::ToolStripMenuItem^ quitToolStripMenuItem;

	private:
		System::ComponentModel::Container^ components;

#pragma region Windows Form Designer generated code
		void InitializeComponent(void)
		{
			this->menuStrip1 = (gcnew System::Windows::Forms::MenuStrip());
			this->sizeToolStripMenuItem = (gcnew System::Windows::Forms::ToolStripMenuItem());
			this->colorToolStripMenuItem = (gcnew System::Windows::Forms::ToolStripMenuItem());
			this->paintToolStripMenuItem = (gcnew System::Windows::Forms::ToolStripMenuItem());
			this->quitToolStripMenuItem = (gcnew System::Windows::Forms::ToolStripMenuItem());
			this->menuStrip1->SuspendLayout();
			this->SuspendLayout();

			// Menu items setup
			this->menuStrip1->ImageScalingSize = System::Drawing::Size(20, 20);
			this->menuStrip1->Items->AddRange(gcnew cli::array< System::Windows::Forms::ToolStripItem^ >(4) {
				this->sizeToolStripMenuItem, this->colorToolStripMenuItem, this->paintToolStripMenuItem, this->quitToolStripMenuItem
			});
			this->menuStrip1->Location = System::Drawing::Point(0, 0);
			this->menuStrip1->Name = L"menuStrip1";
			this->menuStrip1->Size = System::Drawing::Size(832, 28);
			this->menuStrip1->TabIndex = 0;
			this->menuStrip1->Text = L"menuStrip1";

			// sizeToolStripMenuItem
			this->sizeToolStripMenuItem->Name = L"sizeToolStripMenuItem";
			this->sizeToolStripMenuItem->Size = System::Drawing::Size(50, 24);
			this->sizeToolStripMenuItem->Text = L"Size";
			this->sizeToolStripMenuItem->Click += gcnew System::EventHandler(this, &MainForm::sizeToolStripMenuItem_Click);

			// colorToolStripMenuItem
			this->colorToolStripMenuItem->Name = L"colorToolStripMenuItem";
			this->colorToolStripMenuItem->Size = System::Drawing::Size(59, 24);
			this->colorToolStripMenuItem->Text = L"Color";
			this->colorToolStripMenuItem->Click += gcnew System::EventHandler(this, &MainForm::colorToolStripMenuItem_Click);

			// paintToolStripMenuItem
			this->paintToolStripMenuItem->Enabled = false;
			this->paintToolStripMenuItem->Name = L"paintToolStripMenuItem";
			this->paintToolStripMenuItem->Size = System::Drawing::Size(55, 24);
			this->paintToolStripMenuItem->Text = L"Paint";
			this->paintToolStripMenuItem->Click += gcnew System::EventHandler(this, &MainForm::paintToolStripMenuItem_Click);

			// quitToolStripMenuItem
			this->quitToolStripMenuItem->Name = L"quitToolStripMenuItem";
			this->quitToolStripMenuItem->Size = System::Drawing::Size(51, 24);
			this->quitToolStripMenuItem->Text = L"Quit";
			this->quitToolStripMenuItem->Click += gcnew System::EventHandler(this, &MainForm::quitToolStripMenuItem_Click);

			// MainForm
			this->AutoScaleDimensions = System::Drawing::SizeF(8, 16);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->ClientSize = System::Drawing::Size(832, 512);
			this->Controls->Add(this->menuStrip1);
			this->MainMenuStrip = this->menuStrip1;
			this->Name = L"MainForm";
			this->Text = L"MainForm";
			this->Load += gcnew System::EventHandler(this, &MainForm::MainForm_Load);
			this->menuStrip1->ResumeLayout(false);
			this->menuStrip1->PerformLayout();
			this->ResumeLayout(false);
			this->PerformLayout();
		}
#pragma endregion
	private: System::Void MainForm_Load(System::Object^ sender, System::EventArgs^ e) {}

	private: System::Void sizeToolStripMenuItem_Click(System::Object^ sender, System::EventArgs^ e) {
		SizeForm^ sizeForm = gcnew SizeForm();
		if (sizeForm->ShowDialog() == System::Windows::Forms::DialogResult::OK) {
			try {
				rectWidth = sizeForm->GetWidth();
				rectHeight = sizeForm->GetHeight();
				rectColor = sizeForm->GetSelectedColor();

				if (rectWidth <= 0 || rectHeight <= 0) {
					MessageBox::Show("Пожалуйста, введите правильный размер.", "Ошибка!!", MessageBoxButtons::OK, MessageBoxIcon::Error);
					paintToolStripMenuItem->Enabled = false;
				}
				else {
					paintToolStripMenuItem->Enabled = true;
				}
			}
			catch (...) {
				MessageBox::Show("Пожалуйста, введите правильный размер.", "Ошибка!!", MessageBoxButtons::OK, MessageBoxIcon::Error);
			}
		}
	}

	private: System::Void paintToolStripMenuItem_Click(System::Object^ sender, System::EventArgs^ e) {
		Graphics^ g = this->CreateGraphics();
		SolidBrush^ brush = gcnew SolidBrush(rectColor);

		if (rectWidth > this->ClientSize.Width || rectHeight > this->ClientSize.Height) {
			MessageBox::Show("Размер превышает размер окна!", "Ошибка!!", MessageBoxButtons::OK, MessageBoxIcon::Error);
		}
		else {
			g->FillRectangle(brush, 50, 50, rectWidth, rectHeight);
		}
	}

	private: System::Void quitToolStripMenuItem_Click(System::Object^ sender, System::EventArgs^ e) {
		Application::Exit();
	}

	private: System::Void colorToolStripMenuItem_Click(System::Object^ sender, System::EventArgs^ e) {
		ColorDialog^ colorDialog = gcnew ColorDialog();
		if (colorDialog->ShowDialog() == System::Windows::Forms::DialogResult::OK) {
			rectColor = colorDialog->Color;
		}
	}
	};

	int main(array<System::String^>^ args) {
		Application::EnableVisualStyles();
		Application::SetCompatibleTextRenderingDefault(false);
		Zadach4c::MainForm mainForm;
		Application::Run(% mainForm);
		return 0;
	}
}