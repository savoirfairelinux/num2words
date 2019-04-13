## Fixes # by Cassio Batista and Eric Pereira

### Changes proposed in this pull request:

* method `to_date()` implemented for PT\_BR 
* method `to_time()` implemented for PT\_BR 

### Status

- [ ] READY
- [ ] HOLD
- [X] WIP (Work-In-Progress)

### How to verify this change

Usage:
```
./num2words <TIME_FMT> -l pt_BR -t time
./num2words <DATE_FMT> -l pt_BR -t date

	<TIME_FMT>: hh:mm    | h:mm 
	<DATE_FMT>: dd/mm/yy | dd/mm/yy
```

Examples:
```bash
user@host $ ./num2words "2:54"      -l pt_BR -t time
  dois horas e cinquenta e quatro minutos
user@host $ ./num2words "2:00"      -l pt_BR -t time
  dois horas # FIXME: gender issues
user@host $ ./num2words "22:59"     -l pt_BR -t time
  vinte e dois horas e cinquenta e nove minutos
user@host $ ./num2words "23:59"     -l pt_BR -t time
  vinte e três horas e cinquenta e nove minutos
user@host $ ./num2words "11:30 "    -l pt_BR -t time
  onze horas e trinta minutos
user@host $ ./num2words "1:30"      -l pt_BR -t time
  um hora e trinta minutos
user@host $ ./num2words "12/12/12"  -l pt_BR -t date
  doze de dezembro de dois mil e doze
user@host $ ./num2words "3:10"      -l pt_BR -t time
  três horas e dez minutos
user@host $ ./num2words "31/3/2009" -l pt_BR -t date
  trinta e um de março de dois mil e nove
user@host $ ./num2words "31/3/1998" -l pt_BR -t date
  trinta e um de março de mil, novecentos e noventa e oito

```

### Additional notes

*If applicable, explain the rationale behind your change.*

