import requests

def check_loan_approval(dni):
    url = f'https://api.moni.com.ar/api/v4/scoring/pre-score/{dni}'
    headers = {'credential': 'ZGpzOTAzaWZuc2Zpb25kZnNubm5u'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        scoring_result = response.json()
        status = scoring_result.get('status') 
        return status  
    except requests.RequestException as e:
        print(f'Error al consultar API de scoring: {e}')
        return None  