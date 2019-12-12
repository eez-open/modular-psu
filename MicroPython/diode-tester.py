from utime import ticks_ms, ticks_add, ticks_diff, sleep_ms
from eez import scpi, setU, getOutputMode, getI, dlogTraceData

I_SET = 0.01
TIME_STEP_MS = 20

diodeName = scpi('disp:input? "Diode name", TEXT, 1, 20, ""')
if diodeName != None:
    uStep = scpi('disp:input? "U step", NUMBER, VOLT, 0.01, 1, 0.1')
    if uStep != None:
        uStep = float(uStep)
        uBreakdown = None
        try:
            scpi("*SAV 10")
            scpi("MEM:STAT:FREEze ON")

            ch1Model = scpi("SYSTem:CHANnel:MODel? ch1")
            ch2Model = scpi("SYSTem:CHANnel:MODel? ch2")
            if ch1Model.startswith("DCP405") and ch2Model.startswith("DCP405"):
                scpi("INST:COUP:TRAC SER")
            else:
                scpi("INST:COUP:TRAC NONE")

            scpi("INST ch1")

            uMax = float(scpi("VOLT? MAX"))

            scpi("OUTP 0")

            scpi('DISP:INPUT? "Connect your diode on CH1", MENU, BUTTON, "Start"')

            scpi("SENS:CURR:RANG MIN")
            scpi("VOLT 0")
            scpi("CURR " + str(I_SET))

            scpi("SENS:DLOG:TRAC:X:UNIT VOLT")
            scpi("SENS:DLOG:TRAC:X:STEP " + str(uStep))
            scpi("SENS:DLOG:TRAC:X:RANG:MAX " + str(uMax)) # TODO this should be updated if switch to 80V range
            scpi('SENS:DLOG:TRAC:X:LABel "Uset"')
            scpi("SENS:DLOG:TRAC:Y1:UNIT AMPER")
            scpi("SENS:DLOG:TRAC:Y1:RANG:MAX " + str(I_SET))
            scpi('SENS:DLOG:TRAC:Y1:LABel "Imon"')
            scpi('INIT:DLOG:TRACE "/Recordings/' + diodeName + '.dlog"')

            scpi("OUTP 1")

            scpi("DISP:WINDOW:DLOG")

            ch = 1
            t = ticks_ms()
            i = 0
            while True:
                uSet = i * uStep
                
                if uSet > uMax:
                    break

                setU(ch, uSet)
                #scpi("VOLT " + str(uSet))

                t = ticks_add(t, TIME_STEP_MS)
                sleep_ms(ticks_diff(t, ticks_ms()))

                iMon = getI(ch)
                #iMon = scpi("MEAS:CURR?")

                dlogTraceData(iMon)
                #scpi("DLOG:TRACE:DATA " + scpi("MEAS:CURR?"))

                mode = getOutputMode(ch)
                #mode = scpi("OUTP:MODE?")

                print(uSet, iMon, mode)

                #if mode == "CC":
                #    break
                if iMon >= I_SET:
                    uBreakdown = uSet
                    break

                i = i + 1
        finally:
            scpi("ABOR:DLOG")
            scpi("*RCL 10")
            scpi("MEM:STAT:FREEze OFF")

        if uBreakdown != None:
            scpi('DISP:INPUT? "Breakdown voltage is ' + str(uBreakdown) + 'V", MENU, BUTTON, "Close"')
        else:
            scpi('DISP:INPUT? "Breakdown voltage not found", MENU, BUTTON, "Close"')
