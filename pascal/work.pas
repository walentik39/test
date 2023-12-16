program Work;
var x: integer;
begin
	writeln('Сколько вам лет?');
	read(x);
	if (x<25) or (x>45) then
		writeln('не подходит!')
	else
		writeln('Подходит!');
end.
