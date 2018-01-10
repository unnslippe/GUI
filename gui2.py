from tkinter import *
import gui
import tkinter as tk
import pyaudio
import wave
import sys
import mikrofon
import mm
from techmo_sarmata_pyclient.utils.wave_loader import load_wave
from techmo_sarmata_pyclient.service.sarmata_settings import SarmataSettings
from techmo_sarmata_pyclient.service.sarmata_recognize import SarmataRecognizer
from techmo_sarmata_pyclient.service.asr_service_pb2 import ResponseStatus
from address_provider import AddressProvider
import os

def sarmatka():
    def print_results(responses):
        if responses is None:
            print("Empty results - None object")
            return

        for response in responses:
            if response is None:
                print("Empty results - skipping response")
                continue

            print("Received response with status: {}".format(ResponseStatus.Name(response.status)))

            if response.error:
                print("[ERROR]: {}".format(response.error))

            for n, res in enumerate(response.results):
                transcript = " ".join([word.transcript for word in res.words])
                print("[{}.] {} /{}/ ({})".format(n, transcript, res.semantic_interpretation, res.confidence))


    def print_results2(responses):
        info = ["NO_MATCH", 0]
        confidence = 0
        if responses is None:
            print("Empty results - None object")
            return info

        for response in responses:
            if response is None:
                print("Empty results - skipping response")
                continue
            if ResponseStatus.Name(response.status) == "NO_MATCH":
                return info
            if response.error:
                print("[ERROR]: {}".format(response.error))

            for n, res in enumerate(response.results):
                if res.confidence > confidence:
                    confidence = res.confidence
                    info[0] = res.semantic_interpretation
        info[1] = confidence
        return info

    if __name__ == '__main__':
        global informacja_semantyczna
        ap = AddressProvider()
        wave_file = "file.wav"
        grammar_file = "movie_grammar.abnf"
        address = ap.get("sarmata")

        audio = load_wave(wave_file)

        settings = SarmataSettings()
        session_id = os.path.basename(wave_file)
        settings.set_session_id(session_id)
        settings.load_grammar(grammar_file)
        recognizer = SarmataRecognizer(address)
        results = recognizer.recognize(audio, settings)

        info_info = print_results2(results)
        print(info_info)
        informacja_semantyczna=info_info[0]



global count
count=1

def PressedButton():

        mm.play1()

        mikrofon.nagr()

        sarmatka()

        #if info_info[0]=="opis":
        if informacja_semantyczna=="opis":
            mm.play3()
            mikrofon.nagr()
            sarmatka()

        elif informacja_semantyczna=="ogladanie":
            mm.play2()
            mikrofon.nagr()
            sarmatka()


    #if count==2:
        #mm.play()
        #mikrofon.nagr()


root = Tk()
root.title("Filmoteka")
labelx = Label(root, text="Spis Twoich Filmów:", bg="LightBLUE", font="Times 14 underline")
labely = Label(root,text="1.Edward Nożycoręki\n 2.Gnijąca Panna Młoda\n 3.Iluzjonista\n 4.Mroczne Cienie\n 5.Nietykalni\n 6.Planeta Małp\n 7.Podaj Dalej",bg="LightBlue", font="Times 12")

b=Button(root,text=" MIRIAM",command=PressedButton,bg="RED",font="Times 18")
label1=Label(root,text="Aby uruchomić program wciśnij przycisk MIRIAM",bg="White",font="Times 12")
b.pack(side=TOP)
labelx.pack()
labely.pack()
label1.pack(side=BOTTOM,fill=BOTH)
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=BOTH, padx=5, pady=5)
root.mainloop()


#label2.pack()
root.mainloop()