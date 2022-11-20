Rails.application.routes.draw do
  root to: 'marit#index'
  resources :network_devices, only: [:index]
  resources :network_scans, only: [:index, :new]
end

