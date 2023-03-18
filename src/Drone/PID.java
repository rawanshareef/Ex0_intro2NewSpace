package Drone;

public class PID {
    private double P;
    private double I;
    private double D;
    private double P_error = 0;
    private double Integral = 0;


    public PID(double p, double i, double d) {
        super();
        this.P = p;
        this.I = i;
        this.D= d;
        this.P_error = 0;
        this.Integral = 0;

    }




}


