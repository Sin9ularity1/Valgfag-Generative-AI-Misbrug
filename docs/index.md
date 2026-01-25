# AI Chatbot Projekt

Velkommen til mit skoleprojekt omkring udviklingen af en lokal AI-chatbot.

---

## Om Projektet

Dette projekt har til formål at udvikle en **lille transformer-baseret sprogmodel** fra bunden, som kan generere tekst og føre simple chat-samtaler.  

Projektet gennemføres over ca. 3 måneder med ca. 10 timers arbejde om ugen, og giver en praktisk forståelse for opbygning af AI-modeller, tokenisering og transformer-arkitektur.  

---

## Teknologier

- **Python** – programmering og scripting  
- **NumPy** – grundlæggende matematik og datahåndtering  
- **PyTorch** – træning af modellen (valgfrit, men anbefalet)  
- **Ingen eksterne LLM’er** – alt er udviklet lokalt fra bunden  

---

## Projektmål

- Bygge en **transformer-baseret sprogmodel** (1M–10M parametre)  
- Implementere en **Byte-Pair Encoding (BPE)** tokenizer  
- Forberede og behandle tekstdatasæt  
- Udvikle et simpelt chat-interface til interaktion med modellen  
- Lære de tekniske og praktiske aspekter af at bygge en AI fra bunden  

---

## Milepæle og Tidsplan

| Uge | Aktivitet | Output |
|-----|-----------|--------|
| 1–2 | Implementering af BPE tokenizer | `tokenizer.py`, `vocab.json` |
| 3–4 | Datasæt indsamling og forbehandling | `dataset.py`, `train_data.npy` |
| 5–7 | Opbygning af lille transformer | `model.py` |
| 8–10 | Træningsloop og evaluering | `train.py`, `model.pt` |
| 11 | Inferens pipeline og tekstgenerering | `generate.py` |
| 12 | Simpelt chat-interface | `chat.py` |

---

## Metode

Projektet udvikles iterativt med fokus på små delmål. Hver komponent udvikles separat og integreres løbende.  

Der arbejdes med:

- Eksperimentel udvikling  
- Løbende dokumentation  
- Test og evaluering undervejs  

---

## Begrænsninger

Projektet er begrænset af hardware, tid og modelstørrelse. Fokus er på læring og forståelse frem for maksimal performance.

---

## Ekstra Mål (Valgfrit)

- LoRA fine-tuning  
- Grafisk brugerinterface (GUI)  
- Hukommelsesbuffer til modelinteraktion  
- Destillering af modellen for optimering  
- Justering af emotionelle og stilistiske indstillinger  

---

## Forventet Læringsudbytte

Efter projektets gennemførelse forventes følgende færdigheder:

- Dybtgående forståelse af tokenisering  
- Kendskab til transformer-arkitektur  
- Evnen til at bygge et neuralt netværk fra bunden  
- Forståelse af træningsdynamikker  
- Implementering af en minimal, funktionel sprogmodel  

---

## Forfatter

**Reuben Badham**  
Uddannelse: IT-sikkerhed  
Lokation: Danmark  
Formål: Praktisk forståelse af AI-modeller, transformer-arkitektur og udvikling af lokale AI-løsninger
