import datetime
import os.path
import time
from rich.text import Text
from rich.console import Console
from rich.style import Style
from rich.progress import track

console = Console()


class _Print:
    std_color_list = [
        ["0", "[#000000]"],
        ["1", "[#0000AA]"],
        ["2", "[#00AA00]"],
        ["3", "[#00AAAA]"],
        ["4", "[#AA0000]"],
        ["5", "[#AA00AA]"],
        ["6", "[#FFAA00]"],
        ["7", "[#AAAAAA]"],
        ["8", "[#555555]"],
        ["9", "[#5555FF]"],
        ["a", "[#55FF55]"],
        ["b", "[#55FFFF]"],
        ["c", "[#FF5555]"],
        ["d", "[#FF55FF]"],
        ["e", "[#FFFF55]"],
        ["f", "[#FFFFFF]"],
        ["g", "[#DDD605]"],
        ["r", "/"]
    ]

    def __init__(self):
        self.modes = {
            " 信息 ": "black on white",
            " 警告 ": "black on yellow",
            " 错误 ": "red on yellow",
            " 输入 ": "black on white",
            " 成功 ": "white on green",
            " 加载 ": "black on white",
            "  FB  ": "black on #61d6d6"
        }
        self.modes_int = {
            0: " 信息 ",
            1: " 警告 ",
            2: " 错误 ",
            3: " 输入 ",
            4: " 成功 ",
            5: " 加载 ",
            6: "  FB  "
        }
        self.dict_for_color = {
            "0": "#000000",
            "1": "#0000AA",
            "2": "#00AA00",
            "3": "#00AAAA",
            "4": "#AA0000",
            "5": "#AA00AA",
            "6": "#FFAA00",
            "7": "#AAAAAA",
            "8": "#555555",
            "9": "#5555FF",
            "o": "italic",
            "l": "bold",
            "a": "#55FF55",
            "b": "#55FFFF",
            "c": "#FF5555",
            "d": "#FF55FF",
            "e": "#FFFF55",
            "f": "#FFFFFF",
            "g": "#DDD605",
            "u": "underline",
            "s": "strike"
        }
        self.dict_for_color_without_some = {
            "0": "#000000",
            "1": "#0000AA",
            "2": "#00AA00",
            "3": "#00AAAA",
            "4": "#AA0000",
            "5": "#AA00AA",
            "6": "#FFAA00",
            "7": "#AAAAAA",
            "8": "#555555",
            "9": "#5555FF",
            "a": "#55FF55",
            "b": "#55FFFF",
            "c": "#FF5555",
            "d": "#FF55FF",
            "e": "#FFFF55",
            "f": "#FFFFFF",
            "g": "#DDD605"
        }
        self.console = Console(record=True)
        os.makedirs("日志文件", exist_ok=True)

    def _mccolor_console_common(this, text: str):
        return text.replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3",
                                                                                          "\033[0;37;36m").replace("§4",
                                                                                                                   "\033[0;37;31m").replace(
            "§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8",
                                                                                                         "\033[0;37;2m").replace(
            "§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c",
                                                                                                         "\033[0;37;91m").replace(
            "§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r",
                                                                                                        "\033[0m") + "\033[0m"

    def _mccolor_console_st1(self, text: str):
        return text.replace("§1", "\033[7;37;34m").replace("§2", "\033[7;37;32m").replace("§3",
                                                                                          "\033[7;37;36m").replace("§4",
                                                                                                                   "\033[7;37;31m").replace(
            "§5", "\033[7;37;35m").replace("§6", "\033[7;37;33m").replace("§7", "\033[7;37;90m").replace("§8",
                                                                                                         "\033[7;37;2m").replace(
            "§9", "\033[7;37;94m").replace("§a", "\033[7;37;92m").replace("§b", "\033[7;37;96m").replace("§c",
                                                                                                         "\033[7;37;91m").replace(
            "§d", "\033[7;37;95m").replace("§e", "\033[7;37;93m").replace("§f", "\033[7;37;1m").replace("§r",
                                                                                                        "\033[0m") + "\033[0m"

    def MCcolor_converter(self, text: str):
        formatted_text = Text()
        segments = text.split("§r")
        for segment in segments:
            for i in self.dict_for_color:
                if "§" + i in segment:
                    if i == "r":
                        formatted_text.append(segment)
                    else:
                        formatted_text.append(segment.replace("§" + i, ""), style=self.dict_for_color[i])
        return formatted_text

    def log_record(self,log_txt:str = None):
        if log_txt is None:
            log_txt=self.console.export_text()
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        log_filename = os.path.join("日志文件", f"{current_date}.log")
        if not os.path.isfile(log_filename):
            with open(log_filename, "w", encoding="utf-8") as f:
                f.write("")
        with open(log_filename, "a+", encoding="utf-8") as f:
            f.write(log_txt)

    def Style_doll(self,arg_list:list):
        num=-1
        InRange=False
        total_length=len(arg_list)
        Style_list=["o","l","u","s"]
        for arg1 in arg_list:
            num+=1
            italic, bold, underline, strike, color = False, False, False, False, None
            if not arg1:
                continue
            if arg1 in self.had_done_text:
                if arg1 == self.had_done_text[len(self.had_done_text)-1]:
                    self.had_done_text.clear()
                continue
            if (arg1 in Style_list or arg1 in self.dict_for_color) and len(arg1)==1 and not InRange:
                index = num
                num_=0
                total_length_ = len(arg_list)
                can_num=0
                for x in arg_list[num:]:
                    num_+=1
                    if total_length_ >= num + num_ and len(arg_list[num + num_-1]) > 0 and (arg_list[num + num_-1][0] in Style_list and len(arg_list[num + num_-1]) == 1):
                        if total_length_ >= num +num_+1 and len(arg_list[num + num_]) > 0 and arg_list[num + num_][0] in self.dict_for_color_without_some:
                            can_num += 1
                            break
                        can_num+=1
                if 1:
                    end=num+can_num
                    InRange = True
                    for i in range(index,end+1):
                        if arg_list[i][0] =="o":italic=True
                        elif arg_list[i][0] =="l":bold=True
                        elif arg_list[i][0] =="u":underline=True
                        elif arg_list[i][0] =="s":strike=True
                        elif arg_list[i][0] in self.dict_for_color:color=self.dict_for_color[arg_list[i][0]]
                        self.had_done_text.append(arg_list[i])
                    # print(self.had_done_text)
                    self.text.append(text=arg_list[end][1:],style=Style(italic=italic,bold=bold,underline=underline,strike=strike,color=color))
                    # self.console.print(self.text)
                InRange=False
            elif len(arg1)>0 and arg1[0] in self.dict_for_color and not InRange:
                self.text.append(text=arg1[1:],style=self.dict_for_color[arg1[0]])

    def check_mode(self, mode: int | str = 0, back: str = "white",sep=" ",*args):
        if "§" in back:
            back = self.dict_for_color[back[1]]
        if "§b  FB  §r" in args or "§b  FB  " in args:
            self.FBmode = True
        elif "§d 加载 " in args:
            self.text.append(text=" 加载 ", style=f"#FF55FF on {back}")
        else:
            if isinstance(mode, int):
                if mode in self.modes_int:
                    self.text.append(text=self.modes_int[mode], style=self.modes[self.modes_int[mode]])
            else:
                if "§" in mode:
                    for i in self.dict_for_color:
                        if "§" + i in mode:
                            self.text.append(text=mode.replace("§" + i, ""),
                                             style=self.dict_for_color[i] + f" on {back}")
                    if "§r" in mode:
                        self.text.append(text=mode.replace("§r", ""), style="black on white")

    def print_with_info(self, *args, mode: int | str = 0, back: str = "white", countdown=None, endmsg="倒计时结束",
                        sep=" ",
                        end="\n"):
        """
        # 默认已开启日志记录
        你可以输出任意形式的东西
        mode表: -- 你也可以自己定义颜色
            1:[black on white] 信息 [/black on white]
            2:[black on yellow] 警告 [/black on yellow] [yellow]
            3:[red on yellow] 错误 [/red on yellow] [red]
            4:[black on white] 输入 [/black on white]
            5:[white on green] 成功 [/white on green]
            6:[black on white] 加载 [/black on white]
            7:[yellow on white]  FB  [/yellow on white]
        back:框的背景颜色,支持rich颜色以及§
        countdown:int 倒计时,输入时间
        endmsg:结束后输出文本

        """
        self.text = Text()
        self.text.append(text=f"[{datetime.datetime.now().strftime('%H:%M:%S')}] ")
        self.had_done_text = []
        self.FBmode = False
        self.check_mode(mode, back,sep,*args)
        for arg in args:
            if self.FBmode and ("§b  FB  §r" == arg or "§b  FB  " == arg):
                break
            if "§d 加载 " == arg:
                break
            self.text.append(sep)
            if arg in self.had_done_text:
                continue
            if isinstance(arg, str):
                if "Traceback" in arg or "Error" in arg or "error" in arg:
                    self.console.print(arg)
                elif "§" in arg:
                    self.Style_doll(arg_list=arg.split("§"))
                else:
                    self.text.append(text=arg)
            else:
                self.text.append(text=arg)

        if countdown is not None:
            for i in track(range(countdown), description=args[0]):
                time.sleep(0.2)
            self.console.print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] ", style="", end="")
            self.console.print(self.modes_int[0], style=self.modes[self.modes_int[0]], end="")
            self.console.print(f" [cyan]{endmsg}[/cyan]")  # 倒计时后的留言
        else:
            if self.FBmode:  # 就***的离谱,FB的输出内容rich会自动转行,而且禁用了自动转行还是不行
                print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] ",end="")
                self.console.print(self.modes_int[6], style=self.modes[self.modes_int[6]], end="")
                print(*args[:1])
                self.log_record(f"[{datetime.datetime.now().strftime('%H:%M:%S')}]  FB {''.join(args[:1])}")
            else:
                self.console.print(self.text, end=end)
        self.log_record()

    def input(self, text: str = "") -> str:
        self.print_with_info(text, end="", mode=3)
        return input()

    def print_err(self, text):
        self.print_with_info(f"§c{text}", mode=2)

    def print_inf(self, *args):
        self.print_with_info(*args)

    def print_suc(self, text):
        self.print_with_info(text, mode=4)

    def print_war(self, text):
        self.print_with_info(f"§6{text}", mode=1)

    def fmt_info(self, text: str, info: str):
        output_txts = []
        for text_line in str(text).split("\n"):
            output_txts.append(datetime.datetime.now().strftime("[%H:%M:%S] ") + self._mccolor_console_st1(
                info) + " " + self._mccolor_console_common(text_line))
        return "\n".join(output_txts)


Print = _Print()
