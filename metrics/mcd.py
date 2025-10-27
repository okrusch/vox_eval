from pymcd.mcd import Calculate_MCD

def get_mcd(ref_path, syn_path):
    mcd_toolbox = Calculate_MCD(MCD_mode="dtw")
    return mcd_toolbox.calculate_mcd(ref_path, syn_path)


#print(get_mcd("test_metrics/ref.wav", "test_metrics/gradtts.wav"))
