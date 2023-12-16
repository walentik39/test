program Dey;
var d: integer;
begin
	writeln('День недели');
	read(d);
	if (d = 1) or (d = 4) then
		writeln('Да')
	else
		writeln('Нет!');
end.
