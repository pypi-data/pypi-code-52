import casadi as cas
from ..casadi_helpers import sind, cosd

def solar_flux_outside_atmosphere_normal(day_of_year):
    """
    Normal solar flux at the top of the atmosphere (variation due to orbital eccentricity)
    :param day_of_year: Julian day (1 == Jan. 1, 365 == Dec. 31)
    :return: Solar flux [W/m^2]
    """
    # Space effects
    # # Source: https://www.itacanet.org/the-sun-as-a-source-of-energy/part-2-solar-energy-reaching-the-earths-surface/#2.1.-The-Solar-Constant
    # solar_flux_outside_atmosphere_normal = 1367 * (1 + 0.034 * cas.cos(2 * cas.pi * (day_of_year / 365.25)))  # W/m^2; variation due to orbital eccentricity
    # Source: https://www.pveducation.org/pvcdrom/properties-of-sunlight/solar-radiation-outside-the-earths-atmosphere
    return 1366 * (
            1 + 0.033 * cosd(360 * (day_of_year - 2) / 365))  # W/m^2; variation due to orbital eccentricity


def declination_angle(day_of_year):
    """
    Declination angle, in degrees, as a func. of day of year. (Seasonality)
    :param day_of_year: Julian day (1 == Jan. 1, 365 == Dec. 31)
    :return: Declination angle [deg]
    """
    # Declination (seasonality)
    # Source: https://www.pveducation.org/pvcdrom/properties-of-sunlight/declination-angle
    return -23.45 * cosd(360 / 365 * (day_of_year + 10))  # in degrees


def solar_elevation_angle(latitude, day_of_year, time):
    """
    Elevation angle of the sun [degrees] for a local observer.
    :param latitude: Latitude [degrees]
    :param day_of_year: Julian day (1 == Jan. 1, 365 == Dec. 31)
    :param time: Time after local solar noon [seconds]
    :return: Solar elevation angle [degrees] (angle between horizon and sun). Returns 0 if the sun is below the horizon.
    """

    # Solar elevation angle (including seasonality, latitude, and time of day)
    # Source: https://www.pveducation.org/pvcdrom/properties-of-sunlight/elevation-angle
    declination = declination_angle(day_of_year)

    solar_elevation_angle = cas.asin(
        sind(declination) * sind(latitude) +
        cosd(declination) * cosd(latitude) * cosd(time / 86400 * 360)
    ) * 180 / cas.pi  # in degrees
    solar_elevation_angle = cas.fmax(solar_elevation_angle, 0)
    return solar_elevation_angle


def incidence_angle_function(latitude, day_of_year, time, scattering=False):
    """
    What is the fraction of insolation that a horizontal surface will receive as a function of sun position in the sky?
    :param latitude: Latitude [degrees]
    :param day_of_year: Julian day (1 == Jan. 1, 365 == Dec. 31)
    :param time: Time since (local) solar noon [seconds]
    :param scattering: Boolean: include scattering effects at very low angles?
    """
    # Old description:
    # To first-order, this is true. In class, Kevin Uleck claimed that you have higher-than-cosine losses at extreme angles,
    # since you get reflection losses. However, an experiment by Sharma appears to not reproduce this finding, showing only a
    # 0.4-percentage-point drop in cell efficiency from 0 to 60 degrees. So, for now, we'll just say it's a cosine loss.
    # Sharma: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6611928/

    elevation_angle = solar_elevation_angle(latitude, day_of_year, time)

    theta = 90 - elevation_angle  # Angle between panel normal and the sun, in degrees
    cosine_factor = cosd(theta)

    if not scattering:
        return cosine_factor
    else:
        # Calculate scattering knockdown (See C:\Users\User\Google Drive\School\Grad School\2020 Spring\16-885\Solar Panel Scattering Rough Fit)
        theta_rad = theta * cas.pi / 180
        # Model 1
        c = (
            0.27891510500505767300438719757949,
            -0.015994330894744987481281839336589,
            -19.707332432605799255043166340329,
            -0.66260979582573353852126274432521
        )
        scattering_factor = c[0] + c[3] * theta_rad + cas.exp(
            c[1] * (
                    cas.tan(theta_rad - 1e-8) + c[2] * theta_rad
            )
        )
        # Model 2
        # c = (
        #     -0.04636,
        #     -0.3171
        # )
        # scattering_factor = cas.exp(
        #     c[0] * (
        #         cas.tan(theta_rad-1e-8) + c[1] * theta_rad
        #     )
        # )
        # Model 3
        # p1 = -21.74
        # p2 = 282.6
        # p3 = -1538
        # p4 = 1786
        # q1 = -923.2
        # q2 = 1456
        # x = theta_rad
        # scattering_factor = ((p1*x**3 + p2*x**2 + p3*x + p4) /
        #            (x**2 + q1*x + q2))

        # scattering_factor = cas.fmin(cas.fmax(scattering_factor, 0), 1)

        return cosine_factor * scattering_factor


def solar_flux_on_horizontal(latitude, day_of_year, time, scattering=False):
    """
    What is the solar flux on a horizontal surface for some given conditions?
    :param latitude: Latitude [degrees]
    :param day_of_year: Julian day (1 == Jan. 1, 365 == Dec. 31)
    :param time: Time since (local) solar noon [seconds]
    :param scattering: Boolean: include scattering effects at very low angles?
    :return:
    """
    return (
            solar_flux_outside_atmosphere_normal(day_of_year) *
            incidence_angle_function(latitude, day_of_year, time, scattering)
    )


if __name__ == "__main__":
    # Run some checks
    import plotly.graph_objects as go
    import numpy  as np

    latitudes = np.linspace(26, 49, 200)
    day_of_years = np.arange(0, 365) + 1
    times = np.linspace(0, 86400, 400)


    # Times, Latitudes = np.meshgrid(times, latitudes, indexing="ij")
    # fluxes = np.array(solar_flux_on_horizontal(Latitudes, 244, Times))
    # fig = go.Figure(
    #     data=[
    #         go.Surface(
    #             x=Times / 3600,
    #             y=Latitudes,
    #             z=fluxes,
    #         )
    #     ],
    # )
    # fig.update_layout(
    #     scene=dict(
    #         xaxis=dict(title="Time after Solar Noon [hours]"),
    #         yaxis=dict(title="Latitude [deg]"),
    #         zaxis=dict(title="Solar Flux [W/m^2]"),
    #         camera=dict(
    #             eye=dict(x=-1, y=-1, z=1)
    #         )
    #     ),
    #     title="Solar Flux on Horizontal",
    # )
    # fig.show()
    #
    # fig = go.Figure(
    #     data=[
    #         go.Contour(
    #             z=fluxes.T,
    #             x=times/3600,
    #             y=latitudes,
    #             colorbar=dict(
    #                 title="Solar Flux [W/m^2]"
    #             ),
    #             colorscale="Viridis",
    #         )
    #     ]
    # )
    # fig.update_layout(
    #     scene=dict(
    #         xaxis=dict(title="Hours after Solar Noon [hours]"),
    #         yaxis=dict(title="Latitude [deg]"),
    #     ),
    #     title="Solar Flux on Horizontal",
    #     xaxis_title="Time after Solar Noon [hours]",
    #     yaxis_title="Latitude [deg]",
    # )
    # fig.show()

    import matplotlib.pyplot as plt
    import matplotlib.style as style
    style.use("fivethirtyeight")
    # style.use("seaborn")
    # style.use("ggplot")

    plt.figure()
    lats_to_plot = [26, 49]
    lats_to_plot = np.linspace(0, 90, 7)
    colors = plt.cm.rainbow(np.linspace(0,1,len(lats_to_plot)))[::-1]
    [
        plt.plot(
            times/3600,
            solar_flux_on_horizontal(lats_to_plot[i], 244, times),
            label="%iN Latitude" % lats_to_plot[i],
            color=colors[i]
        ) for i in range(len(lats_to_plot))
    ]
    plt.grid(True)
    plt.legend()
    plt.title("Solar Flux on a Horizontal Surface (Aug. 31)")
    plt.xlabel("Time after Solar Noon [hours]")
    plt.ylabel(r"Solar Flux [W/m$^2$]")
    plt.tight_layout()
    plt.show()