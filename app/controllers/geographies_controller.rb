class GeographiesController < ApplicationController

  def index
    @geographies = Project.find(params[:project_id]).geographies
  end
end
