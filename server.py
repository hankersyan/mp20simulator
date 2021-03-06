# -*- coding: utf-8 -*-
import socket
import packets
import time
from multiprocessing import Process
import datetime

localIP     = "0.0.0.0"
localPort   = 24105
bufferSize  = 1024
absoluteDate = 0

def startSendData(serv, clientAddress):
  nu = 0
  wa = 0
  address = clientAddress

  while(True):
    # poll request
    print('Waiting poll request')
    serv.settimeout(10)
    bytesAddressPair = serv.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    if (len(message) > 34):
      if (message[33] == 0x06):
        # numeric
        print('accept poll request of numeric')
        if (0 == nu):
          serv.sendto(packets.rsp_nu_1_no_1, address)
          serv.sendto(packets.rsp_nu_1_no_2, address)
          serv.sendto(packets.rsp_nu_1_no_3, address)
        elif (1 == nu):
          serv.sendto(packets.rsp_nu_2_no_1, address)
          serv.sendto(packets.rsp_nu_2_no_2, address)
          serv.sendto(packets.rsp_nu_2_no_3, address)
        elif (2 == nu):
          serv.sendto(packets.rsp_nu_3_no_1, address)
          serv.sendto(packets.rsp_nu_3_no_2, address)
          serv.sendto(packets.rsp_nu_3_no_3, address)
        elif (3 == nu):
          serv.sendto(packets.rsp_nu_4_no_1, address)
          serv.sendto(packets.rsp_nu_4_no_2, address)
          serv.sendto(packets.rsp_nu_4_no_3, address)
        elif (4 == nu):
          serv.sendto(packets.rsp_nu_5_no_1, address)
          serv.sendto(packets.rsp_nu_5_no_2, address)
          serv.sendto(packets.rsp_nu_5_no_3, address)
        elif (5 == nu):
          serv.sendto(packets.rsp_nu_6_no_1, address)
          serv.sendto(packets.rsp_nu_6_no_2, address)
          serv.sendto(packets.rsp_nu_6_no_3, address)
        elif (6 == nu):
          serv.sendto(packets.rsp_nu_7_no_1, address)
          serv.sendto(packets.rsp_nu_7_no_2, address)
          serv.sendto(packets.rsp_nu_7_no_3, address)
        elif (7 == nu):
          serv.sendto(packets.rsp_nu_8_no_1, address)
          serv.sendto(packets.rsp_nu_8_no_2, address)
          serv.sendto(packets.rsp_nu_8_no_3, address)
        elif (8 == nu):
          serv.sendto(packets.rsp_nu_9_no_1, address)
          serv.sendto(packets.rsp_nu_9_no_2, address)
          serv.sendto(packets.rsp_nu_9_no_3, address)
        else:
          serv.sendto(packets.rsp_nu_10_no_1, address)
          serv.sendto(packets.rsp_nu_10_no_2, address)
          serv.sendto(packets.rsp_nu_10_no_3, address)
          serv.sendto(packets.rsp_nu_10_no_4, address)
        nu += 1
        nu = nu % 10
      elif (message[33] == 0x09):
        # wave
        print('accept poll request of wave')
        if (0 == wa):
          serv.sendto(packets.rsp_wave_1_no_1, address)
        elif (1 == wa):
          serv.sendto(packets.rsp_wave_2_no_1, address)
        elif (2 == wa):
          serv.sendto(packets.rsp_wave_3_no_1, address)
          serv.sendto(packets.rsp_wave_3_no_2, address)
          serv.sendto(packets.rsp_wave_3_no_3, address)
        elif (3 == wa):
          serv.sendto(packets.rsp_wave_4_no_1, address)
          serv.sendto(packets.rsp_wave_4_no_2, address)
          serv.sendto(packets.rsp_wave_4_no_3, address)
          serv.sendto(packets.rsp_wave_4_no_4, address)
        elif (4 == wa):
          serv.sendto(packets.rsp_wave_5_no_1, address)
          serv.sendto(packets.rsp_wave_5_no_2, address)
          serv.sendto(packets.rsp_wave_5_no_3, address)
          serv.sendto(packets.rsp_wave_5_no_4, address)
        elif (5 == wa):
          serv.sendto(packets.rsp_wave_6_no_1, address)
          serv.sendto(packets.rsp_wave_6_no_2, address)
          serv.sendto(packets.rsp_wave_6_no_3, address)
          serv.sendto(packets.rsp_wave_6_no_4, address)
        elif (6 == wa):
          serv.sendto(packets.rsp_wave_7_no_1, address)
          serv.sendto(packets.rsp_wave_7_no_2, address)
          serv.sendto(packets.rsp_wave_7_no_3, address)
          serv.sendto(packets.rsp_wave_7_no_4, address)
        elif (7 == wa):
          serv.sendto(packets.rsp_wave_8_no_1, address)
          serv.sendto(packets.rsp_wave_8_no_2, address)
          serv.sendto(packets.rsp_wave_8_no_3, address)
          serv.sendto(packets.rsp_wave_8_no_4, address)
        elif (8 == wa):
          serv.sendto(packets.rsp_wave_9_no_1, address)
          serv.sendto(packets.rsp_wave_9_no_2, address)
          serv.sendto(packets.rsp_wave_9_no_3, address)
          serv.sendto(packets.rsp_wave_9_no_4, address)
        else:
          serv.sendto(packets.rsp_wave_10_no_1, address)
          serv.sendto(packets.rsp_wave_10_no_2, address)
          serv.sendto(packets.rsp_wave_10_no_3, address)
          serv.sendto(packets.rsp_wave_10_no_4, address)
        wa += 1
        wa = wa % 10

def startListen(serv):
  print('Waiting association request at ' + str(datetime.datetime.now()))
  serv.settimeout(None)
  bytesAddressPair = serv.recvfrom(bufferSize)
  try:
    serv.settimeout(10)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    ba = bytearray(message)

    if ba == packets.association_request_ba:
      print('Accept Association Request')
      serv.sendto(packets.association_response, address)

      absoluteDate = datetime.datetime.now()
      mdsCreateEventReport = packets.mds_create_event_report
      idxOfAbsTime = 0
      for i in range(len(mdsCreateEventReport) - 16):
        if mdsCreateEventReport[i] == 0x09 and mdsCreateEventReport[i+1] == 0x87 and mdsCreateEventReport[i+2] == 0x00 and mdsCreateEventReport[i+3] == 0x08:
          idxOfAbsTime = i
          break

      # BCD encodes 20 => 0x20
      tmp = [int(str(int(absoluteDate.year/100)), 16),
        int(str(absoluteDate.year%100), 16),
        int(str(absoluteDate.month), 16),
        int(str(absoluteDate.day), 16),
        int(str(absoluteDate.hour), 16),
        int(str(absoluteDate.minute), 16),
        int(str(absoluteDate.second), 16),0]
      # tmp = [int(absoluteDate.year/100), absoluteDate.year%100, absoluteDate.month, 
      #   absoluteDate.day, absoluteDate.hour, absoluteDate.minute, absoluteDate.second, 0]
      print(type(mdsCreateEventReport[:idxOfAbsTime+4]))
      print(type(bytearray(tmp)))
      print(type(mdsCreateEventReport[idxOfAbsTime+11:]))
      mdsCreateEventReport = mdsCreateEventReport[:idxOfAbsTime+4] + bytearray(tmp) + mdsCreateEventReport[idxOfAbsTime+12:]

      serv.sendto(mdsCreateEventReport, address)

      # mds create event result
      print('Waiting mds create event result')
      bytesAddressPair = serv.recvfrom(bufferSize)
      # rtsa priority list
      print('Waiting rtsa priority list')
      bytesAddressPair = serv.recvfrom(bufferSize)
      # set rtsa priority list
      print('Waiting set rtsa priority list')
      bytesAddressPair = serv.recvfrom(bufferSize)

      serv.sendto(packets.rsp_get_result, address)
      serv.sendto(packets.rsp_confirmed_set_result, address)

      startSendData(serv, address)
  except socket.timeout:
    print('timeout')
  else:
    print('Unknown Error')


if __name__ == '__main__':
  # Create a datagram socket
  serv = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

  # Bind to address and ip
  serv.bind((localIP, localPort))

  while(True):
    startListen(serv)
    time.sleep(3)
