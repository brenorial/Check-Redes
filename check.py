import customtkinter as ctk
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# Função para verificar os links
def verificar_links():
    urls = [
        "http://10.80.8.23:4200/login",
        "http://10.80.8.23/ppd/",
        "http://10.69.112.17:8080/oviyam2/",
        "https://suporte.riosaude.rio.br/",
        "http://10.69.112.15:8080/vitai/pages/login.do"
    ]
    
    results = []
    driver = webdriver.Chrome()

    for url in urls:
        try:
            driver.get(url)
            results.append(f"{url} - OK")
        except WebDriverException:
            results.append(f"{url} - Falhou")
    
    driver.quit()
    
    result_text = "\n".join(results)
    show_custom_messagebox("Resultados da Verificação", result_text)

# Função para exibir um messagebox customizado com customtkinter
def show_custom_messagebox(title, message):
    messagebox = ctk.CTkToplevel()
    messagebox.title(title)
    
    frame = ctk.CTkFrame(master=messagebox)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    label = ctk.CTkLabel(master=frame, text=message, font=("Helvetica", 14))
    label.pack(pady=12, padx=10)
    
    button = ctk.CTkButton(master=frame, text="OK", command=messagebox.destroy, font=("Helvetica", 14, "bold"))
    button.pack(pady=12, padx=10)

# Criar a interface gráfica com customtkinter
ctk.set_appearance_mode("dark")  # Modos: "System" (padrão), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (padrão), "green", "dark-blue"

root = ctk.CTk()
root.title("Checklist - Links")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Verificador de Links", font=("Helvetica", 24, "bold"))
label.pack(pady=12, padx=10)

check_button = ctk.CTkButton(master=frame, text="Verificar", command=verificar_links, font=("Helvetica", 14))
check_button.pack(pady=12, padx=10)

developed_label = ctk.CTkLabel(master=frame, text="Desenvolvido por Rial", font=("Helvetica", 8))
developed_label.pack(pady=6, padx=10)

root.mainloop()
