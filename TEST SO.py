import tkinter as tk
from tkinter import messagebox
import random

class LinuxQuiz:

    def __init__(self, root):

        self.root = root
        self.root.title("Certificación Linux - Examen Estudiantil")
        self.root.geometry("700x600")
        self.root.configure(bg="#1a1a1a")

        self.student_name = ""

        # ===============================
        # BANCO DE PREGUNTAS
        # ===============================
        self.all_questions = [

            {"q": "¿Qué comando se usa para ver el directorio actual?",
             "o": ["ls", "pwd", "cd", "dir"],
             "a": "pwd"},

            {"q": "¿Cómo se listan archivos ocultos?",
             "o": ["ls -a", "ls -h", "ls -l", "ls -x"],
             "a": "ls -a"},

            {"q": "Comando para cambiar permisos de archivos:",
             "o": ["chown", "chattr", "chmod", "perm"],
             "a": "chmod"},

            {"q": "¿Qué comando muestra el uso de disco?",
             "o": ["df", "du", "free", "top"],
             "a": "df"},

            {"q": "Comando para buscar texto dentro de archivos:",
             "o": ["find", "locate", "grep", "search"],
             "a": "grep"},

            {"q": "¿Cómo se crea una carpeta nueva?",
             "o": ["touch", "mkdir", "newdir", "md"],
             "a": "mkdir"},

            {"q": "Comando para ver procesos en tiempo real:",
             "o": ["ps", "top", "kill", "jobs"],
             "a": "top"},

            {"q": "¿Qué comando muestra las últimas líneas de un archivo?",
             "o": ["head", "cat", "tail", "more"],
             "a": "tail"},

            {"q": "Comando para cambiar el dueño de un archivo:",
             "o": ["chmod", "chown", "useradd", "su"],
             "a": "chown"},

            {"q": "¿Cómo se borra un directorio con contenido?",
             "o": ["rm", "del", "rmdir", "rm -r"],
             "a": "rm -r"},

            {"q": "Comando para ver la configuración de red:",
             "o": ["ifconfig", "ip addr", "netstat", "route"],
             "a": "ip addr"},

            {"q": "Muestra el manual de un comando:",
             "o": ["help", "info", "man", "guide"],
             "a": "man"},

            {"q": "¿Qué comando apaga el sistema inmediatamente?",
             "o": ["halt", "stop", "shutdown now", "exit"],
             "a": "shutdown now"},

            {"q": "Comando para crear un archivo vacío:",
             "o": ["new", "create", "touch", "file"],
             "a": "touch"},

            {"q": "Muestra el espacio usado por directorios:",
             "o": ["df", "du", "free", "stat"],
             "a": "du"},

            {"q": "¿Cómo se ven las variables de entorno?",
             "o": ["env", "echo", "var", "set"],
             "a": "env"},

            {"q": "Comando para comprimir archivos en .tar:",
             "o": ["zip", "tar", "gzip", "compress"],
             "a": "tar"},

            {"q": "Muestra quién está conectado al sistema:",
             "o": ["who", "users", "id", "finger"],
             "a": "who"},

            {"q": "Comando para buscar archivos por nombre:",
             "o": ["grep", "find", "search", "where"],
             "a": "find"},

            {"q": "Muestra la memoria RAM libre y usada:",
             "o": ["mem", "free", "top", "df"],
             "a": "free"},

            {"q": "¿Qué comando edita el cron del usuario?",
             "o": ["crontab -e", "cron -edit", "sched", "at"],
             "a": "crontab -e"},

            {"q": "Comando para mover o renombrar archivos:",
             "o": ["cp", "mv", "rn", "move"],
             "a": "mv"},

            {"q": "Muestra el nombre del nodo (hostname):",
             "o": ["uname -n", "whoami", "host", "dns"],
             "a": "uname -n"},

            {"q": "Comando para ver el historial de comandos:",
             "o": ["past", "history", "log", "commands"],
             "a": "history"},

            {"q": "¿Cómo se sale de una sesión de terminal?",
             "o": ["quit", "stop", "exit", "close"],
             "a": "exit"},

            {"q": "Instala paquetes en Debian/Ubuntu:",
             "o": ["yum", "rpm", "dnf", "apt"],
             "a": "apt"},

            {"q": "Muestra la versión del kernel instalada:",
             "o": ["uname -r", "kernel -v", "ver", "os-release"],
             "a": "uname -r"},

            {"q": "Comando para cambiar de usuario:",
             "o": ["su", "user", "change", "login"],
             "a": "su"},

            {"q": "Muestra las conexiones de red activas:",
             "o": ["ping", "netstat", "ssh", "dig"],
             "a": "netstat"},

            {"q": "¿Qué comando cuenta palabras en un archivo?",
             "o": ["count", "wc", "words", "grep -c"],
             "a": "wc"}

        ]

        # ===============================
        # 10 PREGUNTAS ALEATORIAS
        # ===============================
        self.questions = random.sample(self.all_questions, 10)

        self.current_q = 0
        self.score = 0

        # TIEMPO POR PREGUNTA
        self.time_left = 30

        self.timer_job = None

        self.show_login_screen()

    # ==================================
    # PANTALLA LOGIN
    # ==================================
    def show_login_screen(self):

        self.login_frame = tk.Frame(self.root, bg="#1a1a1a")
        self.login_frame.pack(expand=True)

        tk.Label(
            self.login_frame,
            text="SISTEMA DE EXAMEN LINUX",
            font=("Courier", 20, "bold"),
            bg="#1a1a1a",
            fg="#00ff00"
        ).pack(pady=20)

        tk.Label(
            self.login_frame,
            text="Ingrese Nombre del Estudiante",
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="white"
        ).pack(pady=5)

        self.ent_name = tk.Entry(
            self.login_frame,
            font=("Arial", 14),
            width=30,
            justify="center"
        )

        self.ent_name.pack(pady=10)
        self.ent_name.focus_set()

        tk.Button(
            self.login_frame,
            text="COMENZAR EXAMEN",
            font=("Arial", 12, "bold"),
            bg="#00ff00",
            fg="black",
            width=25,
            command=self.start_quiz
        ).pack(pady=20)

    # ==================================
    # INICIAR EXAMEN
    # ==================================
    def start_quiz(self):

        self.student_name = self.ent_name.get().strip()

        if not self.student_name:
            messagebox.showwarning(
                "Atención",
                "Debe ingresar un nombre."
            )
            return

        self.login_frame.destroy()

        self.setup_quiz_ui()
        self.display_question()

    # ==================================
    # INTERFAZ DEL QUIZ
    # ==================================
    def setup_quiz_ui(self):

        self.quiz_frame = tk.Frame(self.root, bg="#1a1a1a")
        self.quiz_frame.pack(fill="both", expand=True)

        self.lbl_student = tk.Label(
            self.quiz_frame,
            text=f"Estudiante: {self.student_name}",
            font=("Arial", 10, "italic"),
            bg="#1a1a1a",
            fg="#aaaaaa"
        )

        self.lbl_student.pack(anchor="nw", padx=10, pady=5)

        self.lbl_timer = tk.Label(
            self.quiz_frame,
            text="00:30",
            font=("Courier", 24, "bold"),
            bg="#1a1a1a",
            fg="#ff4444"
        )

        self.lbl_timer.pack(pady=10)

        self.lbl_question = tk.Label(
            self.quiz_frame,
            text="",
            font=("Arial", 14, "bold"),
            wraplength=600,
            bg="#1a1a1a",
            fg="white",
            height=4
        )

        self.lbl_question.pack(pady=20)

        self.btn_options = []

        for i in range(4):

            btn = tk.Button(
                self.quiz_frame,
                text="",
                font=("Arial", 11),
                width=45,
                height=2,
                bg="#333333",
                fg="white",
                activebackground="#555555",
                command=lambda i=i: self.check_answer(i)
            )

            btn.pack(pady=5)

            self.btn_options.append(btn)

        self.lbl_progress = tk.Label(
            self.quiz_frame,
            text="",
            font=("Arial", 10),
            bg="#1a1a1a",
            fg="#888888"
        )

        self.lbl_progress.pack(side="bottom", pady=20)

    # ==================================
    # MOSTRAR PREGUNTA
    # ==================================
    def display_question(self):

        if self.current_q < len(self.questions):

            self.lbl_progress.config(
                text=f"Pregunta {self.current_q + 1} de 10"
            )

            q_data = self.questions[self.current_q]

            self.lbl_question.config(text=q_data['q'])

            opts = q_data['o'].copy()
            random.shuffle(opts)

            for i, option in enumerate(opts):
                self.btn_options[i].config(text=option)

            self.time_left = 30

            self.update_timer()

        else:
            self.end_quiz()

    # ==================================
    # TEMPORIZADOR
    # ==================================
    def update_timer(self):

        if self.time_left >= 0:

            self.lbl_timer.config(
                text=f"00:{self.time_left:02d}"
            )

            self.time_left -= 1

            self.timer_job = self.root.after(
                1000,
                self.update_timer
            )

        else:
            self.check_answer(-1)

    # ==================================
    # VALIDAR RESPUESTA
    # ==================================
    def check_answer(self, idx):

        if self.timer_job:
            self.root.after_cancel(self.timer_job)

        correct_ans = self.questions[self.current_q]['a']

        if idx == -1:

            messagebox.showwarning(
                "Tiempo agotado",
                f"⏰ Tiempo terminado\n\n"
                f"Respuesta correcta:\n{correct_ans}"
            )

        else:

            selected_ans = self.btn_options[idx].cget("text")

            if selected_ans == correct_ans:

                self.score += 1

                messagebox.showinfo(
                    "Correcto",
                    "✅ Respuesta correcta"
                )

            else:

                messagebox.showerror(
                    "Incorrecto",
                    f"❌ Respuesta incorrecta\n\n"
                    f"Respuesta correcta:\n{correct_ans}"
                )

        self.current_q += 1

        self.display_question()

    # ==================================
    # FINALIZAR EXAMEN
    # ==================================
    def end_quiz(self):

        final_grade = (self.score / 10) * 10

        status = "APROBADO ✅" if final_grade >= 6 else "REPROBADO ❌"

        res_text = (
            f"RESULTADOS DEL EXAMEN\n\n"
            f"Estudiante: {self.student_name}\n"
            f"Aciertos: {self.score} de 10\n"
            f"Calificación: {final_grade:.1f} / 10\n\n"
            f"Estado: {status}"
        )

        messagebox.showinfo(
            "Resultado Final",
            res_text
        )

        self.root.destroy()

# ==================================
# EJECUTAR APP
# ==================================
if __name__ == "__main__":

    root = tk.Tk()

    app = LinuxQuiz(root)

    root.mainloop()