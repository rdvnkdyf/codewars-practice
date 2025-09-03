public class People {

    private int age;
    private String name;
    private String lastName;
    private String city;
    private String job;

    // Sabit adı GREET olarak düzeltildi
    private final String GREET = "hello";

    // Private constructor to enforce object creation via the Builder
    private People(Builder builder) {
        this.age = builder.age;
        this.name = builder.name;
        this.lastName = builder.lastName;
        this.city = builder.city;
        this.job = builder.job;
    }

    // Static method to get a new Builder instance
    public static Builder builder() {
        return new Builder();
    }

    // Public getters for encapsulation
    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }

    public String getLastName() {
        return lastName;
    }

    public String getCity() {
        return city;
    }
    
    public String getJob() {
        return job;
    }
    
    public String greet() {
        // Metot içindeki referans da GREET olarak güncellendi
        return GREET + " my name is " + name;
    }

    // The static nested Builder class
    public static class Builder {
        private int age;
        private String name;
        private String lastName;
        private String city;
        private String job;

        public Builder age(int age) {
            this.age = age;
            return this;
        }

        public Builder name(String name) {
            this.name = name;
            return this;
        }

        public Builder lastName(String lastName) {
            this.lastName = lastName;
            return this;
        }
        
        public Builder city(String city) {
            this.city = city;
            return this;
        }
        
        public Builder job(String job) {
            this.job = job;
            return this;
        }

        // The build method creates the People instance
        public People build() {
            return new People(this);
        }
    }
}