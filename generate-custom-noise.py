def generate_noise_from_psd(psd_func, n_samples, sample_rate): 
    """
    Generate a signal from a given PSD
    
    Parameters:
        psd_func: function
            User's PSD function.
        n_samples: int
            Number of samples to generate.
        sample_rate: float
            sampling rate.
    
    Returns:
        y: ndarray
            Signal generated with the desired PSD.
    """
    # Frequency bins
    freqs = np.fft.rfftfreq(n_samples, d=1/sample_rate)
    valid = freqs > 0.
    freqs = freqs[valid]
    
    #Compute the desired amplitude (sqrt of the PSD)
    psd_target = psd_func(freqs)
    amplitude_spectrum = np.sqrt(psd_target)
    
    #Generate white noise
    random_phases = np.exp(1j * 2 * np.pi * np.random.rand(len(freqs)))
    frequency_domain = amplitude_spectrum * random_phases
    
    #Turn into signal 
    y = np.fft.irfft(frequency_domain, n=n_samples)
    
    #Normalize
    y /= np.std(y)
    
    return(y)
