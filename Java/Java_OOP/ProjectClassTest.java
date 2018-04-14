class ProjectClassTest{

    public static void main (String[] args){
        ProjectClass project1 = new ProjectClass();
        ProjectClass project2 = new ProjectClass("Melissa");
        ProjectClass project3 = new ProjectClass("Melissa", "my name");
        System.out.println(project1);
        System.out.println(project2.getName());
        System.out.println(project3.getDescription());
        project1.setName("Bob");
        project1.setDescription("His name");
        System.out.println(project1.elevatorPitch());
    }

}
