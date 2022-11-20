Rails.application.routes.draw do
  root to: 'marit#index'
  resources :network_devices, only: [:index]
end

