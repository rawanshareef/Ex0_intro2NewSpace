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
   /* public double update(double error, double dt){
        //double control=P*error+D*
        return control;
    }*/




}


