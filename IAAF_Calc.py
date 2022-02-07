from datetime import datetime



SHORT = ['100M', '200M', '400M', '100M HURDLES', '400M HURDLES', 
  '4X100M RELAY']

MID = ['800M', '1500M', '5000M', '10000M', '3000M STEEPLECHASE']

LONG = ['MARATHON', '20KM RACE WALK', '50KM RACE WALK']

FIELD = ['HIGH JUMP', 'POLE VAULT', 'LONG JUMP', 'TRIPLE JUMP', 'SHOT PUT',
  'DISCUS', 'HAMMER', 'JAVELIN', 'DECATHLON', 'HEPTATHLON']

def main():
  event = input('Enter event: ').upper()
  sex = input('Enter sex (M or F): ').upper()
  result = input('Enter result: ')
  print('IAAF Score: ' + str(get_score(event, sex, result)))

def convert_to_seconds(mark, event):

  if event in MID:
    if mark.count('.') == 1:
      t = datetime.strptime(mark, '%M:%S.%f')
    else:
      t = datetime.strptime(mark, '%M:%S')
    return t.minute * 60 + t.second + t.microsecond/1000000

  elif event in LONG:
    if mark.count(':') == 1:
      t = datetime.strptime(mark, '%H:%M')
    elif mark.count('.') == 1:
      t = datetime.strptime(mark, '%H:%M:%S.%f')
    else:
      t = datetime.strptime(mark, '%H:%M:%S')
    return (t.hour * 60 + t.minute) * 60 + t.second + t.microsecond/1000000

  else:
    return float(mark)


def get_score(event, sex, result):
  constants = get_constants(event, sex)
  result = convert_to_seconds(result, event)

  result_shift = constants[0]
  conversion_factor = constants[1]
  point_shift = constants[2]
  
  return round(conversion_factor * (result + result_shift)**2 + point_shift)


def get_constants(event, sex):
  #returns list [result shift, conversion factor, point shift]

  # Men's running events
  if sex == 'M':

    if event == '100M':
      return [-17, 24.63, 0]
    if event == '200M':
      return [-35.5, 5.08, 0]
    if event == '400M':
      return [-79, 1.021, 0]
    if event == '800M':
      return [-182, 0.198, 0]
    if event == '1500M':
      return [-385, 0.04066, 0]
    if event == '5000M':
      return [-1440, 0.002778, 0]
    if event == '10000M':
      return [-3150, 0.000524, 0]
    if event == 'MARATHON':
      return [-15600, 0.0000191, 0]
    if event == '110M HURDLES':
      return [-25.8, 7.66, 0]
    if event == '400M HURDLES':
      return [-95.5, 0.546, 0]
    if event == '3000M STEEPLECHASE':
      return [-1020, 0.004316, 0]
    if event == '20KM RACE WALK':
      return [-11400, 0.00002735, 0]
    if event == '50KM RACE WALK':
      return [-37200, 0.000002124, 0]
    if event == '4X100M RELAY':
      return [-69.5, 1.236, 0]
    if event == '4X400M RELAY':
      return [-334, 0.05026, 0]

    # Men's field events
    if event == 'HIGH JUMP':
      return [11.534, 32.29, -5000]
    if event == 'POLE VAULT':
      return [39.39, 3.042, -5000]
    if event == 'LONG JUMP':
      return [48.41, 1.929, -5000]
    if event == 'TRIPLE JUMP':
      return [98.63, 0.4611, -5000]
    if event == 'SHOT PUT':
      return [687.7, 0.042172, -20000]
    if event == 'DISCUS':
      return [2232.6, 0.004007, -20000]
    if event == 'HAMMER':
      return [2669.4, 0.0028038, -20000]
    if event == 'JAVELIN':
      return [2886.8, 0.0023974, -20000]

    # Combined
    if event == 'DECATHLON':
      return [71170, 0.00000097749, -5000]

  # Women's running events
  if sex == 'F':

    if event == '100M':
      return [-22, 9.92, 0]
    if event == '200M':
      return [-45.5, 2.242, 0]
    if event == '400M':
      return [-110, 0.335, 0]
    if event == '800M':
      return [-250, 0.0688, 0]
    if event == '1500M':
      return [-540, 0.0134, 0]
    if event == '5000M':
      return [-2100, 0.000808, 0]
    if event == '10000M':
      return [-4500, 0.0001712, 0]
    if event == 'MARATHON':
      return [-22800, 0.00000595, 0]
    if event == '100M HURDLES':
      return [-30, 3.98, 0]
    if event == '400M HURDLES':
      return [-130, 0.208567, 0]
    if event == '3000M STEEPLECHASE':
      return [-1510, 0.001323, 0]
    if event == '20KM RACE WALK':
      return [-13200, 0.0000187, 0]
    if event == '4X100M RELAY':
      return [-98, 0.3895, 0]
    if event == '4X400M RELAY':
      return [-480, 0.01562, 0]

    # Women's field events
    if event == 'HIGH JUMP':
      return [10.574, 39.34, -5000]
    if event == 'POLE VAULT':
      return [34.83, 3.953, -5000]
    if event == 'LONG JUMP':
      return [49.24, 1.966, -5000]
    if event == 'TRIPLE JUMP':
      return [105.53, 0.4282, -5000]
    if event == 'SHOT PUT':
      return [657.53, 0.0462, -20000]
    if event == 'DISCUS':
      return [2227.3, 0.0040277, -20000]
    if event == 'HAMMER':
      return [2540, 0.0030965, -20000]
    if event == 'JAVELIN':
      return [2214.9, 0.004073, -20000]

    # Combined
    if event == 'HEPTATHLON':
      return [55990, 0.000001581, -5000]

if __name__ == '__main__':
    main()
