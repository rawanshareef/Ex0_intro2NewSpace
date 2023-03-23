package Drone;

public class PID {
    private double P,I,D,last_error ,Integral ,max_i;

    public PID(double p, double i, double d, double max_i) {
        this.P = p;
        this.I = i;
        this.D= d;
        this.last_error = 0;
        this.Integral = 0;
        this.max_i=0;
    }
    public double constrain(double value, double min, double max){
        if(value < min){
            return min ;
        }
        else if(value > max ){
            return max;
        }
        return value;
    }
    public double update(double error, double dt){
        Integral+=I*error*dt;
        double diff=(error-last_error)/dt;
        double const_integral=constrain(Integral, max_i,-max_i);
        double control=P*error+D*diff+const_integral;
        last_error=error;
        return control;

    }




}


