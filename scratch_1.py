while True:
    x,y=map(int,input("ebter ").split())
    print(x//y)

#READING BYTES EXAMPLE
FileInputStream fis = new FileInputStream("input.txt");
int data;
while ((data = fis.read()) != -1) {
    System.out.print((char) data);
}
fis.close();

#WRITING BYTES
FileOutputStream fos = new FileOutputStream("output.txt");
fos.write("Hello File!".getBytes());
fos.close();

#READ ALL LINES
Path filePath = Paths.get("data.txt");
List<String> lines = Files.readAllLines(filePath);
lines.forEach(System.out::println);

#WRITE TO THE FILE
Path filePath = Paths.get("output.txt");
Files.write(filePath, "Hello NIO.2".getBytes());

#COPY,MOVE,DELETE
Files.copy(Paths.get("a.txt"), Paths.get("b.txt"));
Files.move(Paths.get("old.txt"), Paths.get("new.txt"));
Files.delete(Paths.get("delete.txt"));

